import time
import threading
from producer.producer import SmartMeterProducer
class DeviceThread(threading.Thread):
    def __init__(self, device, kafka_server, topic_name):
        super().__init__()
        self.device = device
        self.producer = SmartMeterProducer(kafka_server, topic_name)

    def run(self):
        try:
            while True:
                data = self.device.generate_usage_data()
                self.producer.send_data(data)
                time.sleep(1)
        except Exception as e:
            print(f"Error in device {self.device}: {e}")
        finally:
            self.producer.close()
