import logging
from threads.device_thread import DeviceThread
import appliances
import config

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    logging.info("Starting the application")
    devices = [appliances.AirConditioner(), appliances.Refrigerator(), appliances.Television()]

    threads = []
    for device in devices:
        try:
            thread = DeviceThread(device, config.KAFKA_SERVER, config.TOPIC_NAME)
            thread.start()
            threads.append(thread)
            logging.info(f"Started thread for {device.name}")
        except Exception as e:
            logging.error(f"Error starting thread for {device.name}: {e}")

    for thread in threads:
        thread.join()
    logging.info("All threads have finished.")

if __name__ == "__main__":
    main()
