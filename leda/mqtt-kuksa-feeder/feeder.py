"""
MQTT → KUKSA Databroker Feeder

Subscribes to vehicle telemetry MQTT topics published by the SHILATE Unity
simulation and forwards the values into the Eclipse KUKSA.val Databroker
using its gRPC interface.

Payload contract (from Unity LedaBroker):
    Topic:   vehicle/{signal}
    Payload: {"value": <float>}   (2 decimal places, invariant culture)

Configuration is loaded from config.json (co-located).
Environment variable overrides:
    MQTT_HOST, MQTT_PORT, KUKSA_HOST, KUKSA_PORT
"""

import json
import logging
import os
import signal
import sys
import time
from pathlib import Path

import paho.mqtt.client as mqtt
from kuksa_client.grpc import Datapoint, DataEntry, EntryUpdate, Field, VSSClient

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging.getLogger("mqtt-kuksa-feeder")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------
CONFIG_PATH = Path(__file__).with_name("config.json")


def load_config() -> dict:
    with open(CONFIG_PATH, "r") as f:
        cfg = json.load(f)

    # Allow environment-variable overrides
    cfg["mqtt"]["host"] = os.environ.get("MQTT_HOST", cfg["mqtt"]["host"])
    cfg["mqtt"]["port"] = int(os.environ.get("MQTT_PORT", cfg["mqtt"]["port"]))
    cfg["kuksa"]["host"] = os.environ.get("KUKSA_HOST", cfg["kuksa"]["host"])
    cfg["kuksa"]["port"] = int(os.environ.get("KUKSA_PORT", cfg["kuksa"]["port"]))
    return cfg


# ---------------------------------------------------------------------------
# KUKSA Databroker writer
# ---------------------------------------------------------------------------
class KuksaWriter:
    """Thin wrapper around kuksa-client VSSClient for current-value writes."""

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._client: VSSClient | None = None

    def connect(self):
        log.info("Connecting to KUKSA Databroker at %s:%d …", self._host, self._port)
        self._client = VSSClient(self._host, self._port)
        self._client.connect()
        log.info("Connected to KUKSA Databroker")

    def set_value(self, vss_path: str, value: float):
        if self._client is None:
            return
        entry = DataEntry(
            vss_path,
            value=Datapoint(value=value),
        )
        updates = (EntryUpdate(entry, (Field.VALUE,)),)
        self._client.set(updates)

    def disconnect(self):
        if self._client is not None:
            self._client.disconnect()
            self._client = None
            log.info("Disconnected from KUKSA Databroker")


# ---------------------------------------------------------------------------
# MQTT subscriber ↔ KUKSA bridge
# ---------------------------------------------------------------------------
class MqttKuksaFeeder:
    def __init__(self, config: dict):
        self._cfg = config
        self._running = True

        # Build topic → VSS path lookup
        self._topic_to_vss: dict[str, str] = {}
        for m in config["mappings"]:
            self._topic_to_vss[m["mqtt_topic"]] = m["vss_path"]
            log.info("  Mapping: %s → %s", m["mqtt_topic"], m["vss_path"])

        self._kuksa = KuksaWriter(
            config["kuksa"]["host"],
            config["kuksa"]["port"],
        )
        self._mqtt_client: mqtt.Client | None = None

    # -- lifecycle ----------------------------------------------------------

    def start(self):
        """Connect to both KUKSA and MQTT, then loop until stopped."""
        self._connect_kuksa()
        self._connect_mqtt()

        log.info("Feeder running – press Ctrl+C to stop")
        try:
            while self._running:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            self.stop()

    def stop(self):
        self._running = False
        if self._mqtt_client is not None:
            self._mqtt_client.loop_stop()
            self._mqtt_client.disconnect()
            log.info("Disconnected from MQTT broker")
        self._kuksa.disconnect()

    # -- KUKSA connection ---------------------------------------------------

    def _connect_kuksa(self):
        while self._running:
            try:
                self._kuksa.connect()
                return
            except Exception as exc:
                log.warning("KUKSA connection failed (%s), retrying in 5 s …", exc)
                time.sleep(5)

    # -- MQTT connection & callbacks ----------------------------------------

    def _connect_mqtt(self):
        mcfg = self._cfg["mqtt"]
        client = mqtt.Client(
            callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
            client_id=mcfg["client_id"],
        )
        client.on_connect = self._on_connect
        client.on_disconnect = self._on_disconnect
        client.on_message = self._on_message
        client.reconnect_delay_set(min_delay=1, max_delay=30)

        log.info(
            "Connecting to MQTT broker at %s:%d …",
            mcfg["host"],
            mcfg["port"],
        )
        client.connect(mcfg["host"], mcfg["port"], keepalive=60)
        client.loop_start()
        self._mqtt_client = client

    def _on_connect(self, client, userdata, flags, reason_code, properties=None):
        if reason_code == 0:
            topic = self._cfg["mqtt"]["topic_root"]
            log.info("Connected to MQTT broker – subscribing to %s", topic)
            client.subscribe(topic)
        else:
            log.error("MQTT connect failed: %s", reason_code)

    def _on_disconnect(self, client, userdata, flags, reason_code, properties=None):
        log.warning("MQTT disconnected (rc=%s), paho will auto-reconnect", reason_code)

    def _on_message(self, client, userdata, msg: mqtt.MQTTMessage):
        vss_path = self._topic_to_vss.get(msg.topic)
        if vss_path is None:
            return  # unknown sub-topic, ignore

        try:
            payload = json.loads(msg.payload)
            value = float(payload["value"])
        except (json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            log.debug("Bad payload on %s: %s (%s)", msg.topic, msg.payload, exc)
            return

        try:
            self._kuksa.set_value(vss_path, value)
        except Exception as exc:
            log.warning("KUKSA write failed for %s: %s", vss_path, exc)
            # Attempt reconnect on next cycle
            try:
                self._kuksa.disconnect()
                self._kuksa.connect()
            except Exception:
                pass


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------
def main():
    log.info("═══════════════════════════════════════════════")
    log.info("  SHILATE  MQTT → KUKSA Databroker Feeder")
    log.info("═══════════════════════════════════════════════")

    config = load_config()

    feeder = MqttKuksaFeeder(config)

    # Graceful shutdown on SIGTERM (container stop)
    def handle_signal(signum, frame):
        log.info("Received signal %d, shutting down …", signum)
        feeder.stop()
        sys.exit(0)

    signal.signal(signal.SIGTERM, handle_signal)

    feeder.start()


if __name__ == "__main__":
    main()
