import json
import time
import random
from kafka import KafkaProducer

def get_data():
    data = {
        'timestamp': int(time.time() * 1000),
        'value': random.randint(0, 100)
    }
    return data

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

while True:
    data = get_data()
    producer.send('data_topic', value=data)
    print(f"Sent: {data}")
    time.sleep(1)
