FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py ./

ENV KUKSA_HOST=127.0.0.1 \
    KUKSA_PORT=55555 \
    MQTT_HOST=localhost \
    MQTT_PORT=1883 \
    SPEED_LIMIT=120 \
    RPM_REDLINE=6500

CMD ["python", "-u", "app.py"]
