FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY feeder.py config.json ./

ENV MQTT_HOST=localhost \
    MQTT_PORT=1883 \
    KUKSA_HOST=127.0.0.1 \
    KUKSA_PORT=55555

CMD ["python", "-u", "feeder.py"]
