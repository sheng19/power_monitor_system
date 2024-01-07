import time
import random

class BaseDevice:
    def __init__(self, name, min_usage, max_usage):
        self.name = name
        self.min_usage = min_usage
        self.max_usage = max_usage

    def generate_usage_data(self):
        return {
            "timestamp": int(time.time()),
            "device": self.name,
            "electricity_usage": random.uniform(self.min_usage, self.max_usage)
        }

class AirConditioner(BaseDevice):
    def __init__(self):
        super().__init__("air_conditioner", 200, 1500)

class Refrigerator(BaseDevice):
    def __init__(self):
        super().__init__("refrigerator", 100, 300)

class Television(BaseDevice):
    def __init__(self):
        super().__init__("television", 50, 200)
