from kafka import KafkaProducer
import json
import logging
import time

class SmartMeterProducer:
    def __init__(self, kafka_server, topic):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_server,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
        self.topic = topic

    def send_data(self, data):
        self.producer.send(self.topic, value=data)
        logging.debug(f"{data}")
        time.sleep(1)

    def close(self):
        self.producer.close()
