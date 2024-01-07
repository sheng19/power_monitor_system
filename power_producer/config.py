import os

KAFKA_SERVER = os.getenv('KAFKA_SERVER', '127.0.0.1:9092')
TOPIC_NAME = os.getenv('TOPIC_NAME', 'smart_meter_data')
