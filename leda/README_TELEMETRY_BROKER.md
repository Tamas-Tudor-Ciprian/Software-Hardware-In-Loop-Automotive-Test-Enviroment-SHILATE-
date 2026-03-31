# Telemetry Broker for Eclipse Leda

This repository adds a simple Rust-based telemetry broker to the `leda` directory. The broker listens for incoming TCP connections and forwards telemetry data between connected clients, enabling data sharing between Eclipse Leda and other applications.

## File Added
- `leda/telemetry_broker.rs`: Rust script implementing the telemetry broker.

## How It Works
- The broker listens on `127.0.0.1:7878`.
- Any client can connect and send telemetry data.
- Data received from one client is forwarded to all other connected clients.
- When a client disconnects, it is removed from the broker's list.

## Usage
1. **Build the broker:**
   - Ensure you have [Rust](https://www.rust-lang.org/tools/install) installed.
   - In the `leda` directory, run:
     ```sh
     rustc telemetry_broker.rs
     ```
2. **Run the broker:**
   ```sh
   ./telemetry_broker.exe
   ```
   (On Linux/Mac: `./telemetry_broker`)
3. **Connect clients:**
   - Any app can connect to `127.0.0.1:7878` via TCP to send/receive telemetry data.

## Example
- Start the broker.
- Use `netcat` or a custom app to connect:
  ```sh
  nc 127.0.0.1 7878
  ```
- Data sent from one client will be received by all others.

## Notes
- This is a minimal example for demonstration and prototyping.
- For production, consider authentication, error handling, and protocol design.

## Changes Implemented
- Added `telemetry_broker.rs` to `leda/`.
- Updated documentation with usage instructions.
