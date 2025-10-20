from kafka import KafkaProducer
import json, time, random

# Configurar el productor Kafka
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

print("=== Enviando datos simulados a Kafka ===")

while True:
    data = {
        'sensor_id': random.randint(1, 10),
        'temperature': round(random.uniform(20.0, 30.0), 2),
        'humidity': round(random.uniform(30.0, 70.0), 2),
        'timestamp': int(time.time())
    }
    producer.send('sensores', value=data)
    print(f"Sent: {data}")
    time.sleep(1)
