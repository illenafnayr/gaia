# batch.py
import time
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from sensorscripts.DataLogger import DataLogger
from sensorscripts.TSL2591X.TSLX2591XDataLogger import LightSensorDataLogger


class BatchService:
    def __init__(self, csv_file_path):
        self.csv_file_path = csv_file_path
        self.light_sensor_logger = LightSensorDataLogger()
        # self.temp_sensor_logger = TemperatureSensorDataLogger
        self.light_data_logger = DataLogger(self.light_sensor_logger, self.csv_file_path)

    def run(self, num_rounds=4, interval_minutes=0.1):
        for _ in range(num_rounds):
            self.log_data_round()
            time.sleep(60 * interval_minutes)

    def log_data_round(self):
        print("Logging data round...")
        # Log light sensor data
        self.light_data_logger.add_data()

        # Log temperature sensor data
        # self.temp_data_logger.add_data()

        # Add timestamp and save to CSV
        self.light_data_logger.add_timestamp()
        self.light_data_logger.save_to_csv()

if __name__ == "__main__":
    csv_file_path = 'your_data.csv'
    batch_service = BatchService(csv_file_path)
    batch_service.run()
