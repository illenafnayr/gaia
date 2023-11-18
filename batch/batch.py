# batch.py
import datetime
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

    def run(self, num_rounds=1000, interval_minutes=15):
        for i in range(num_rounds):
            self.log_data_round(i)
            time.sleep(60 * interval_minutes)

    def log_data_round(self, i):
        print("row #: {i}")
        # Log light sensor data
        self.light_data_logger.add_data()

        # Log temperature sensor data
        # self.temp_data_logger.add_data()

        # Add timestamp to all data
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.light_data_logger.add_timestamp(timestamp)

        # Save to CSV
        self.light_data_logger.save_to_csv()

if __name__ == "__main__":
    csv_file_path = 'light-sensor-data.csv'
    batch_service = BatchService(csv_file_path)
    batch_service.run()
