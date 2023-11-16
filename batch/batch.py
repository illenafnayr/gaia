# batch.py
import time
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from sensorscripts.DataLogger import DataLogger
from sensorscripts.TSL2591X.TSLX2591XDataLogger import LightSensorDataLogger


def my_batch_action():
    # Replace this with the action you want to perform
    custom_header = ['Timestamp', 'Lux', 'Infrared', 'Visible', 'FullSpectrum']
    logger = DataLogger(LightSensorDataLogger, csv_file_path='light-sensor-data.csv', header=custom_header)
    logger.log_sensor_data()

def run_batch_job(interval_seconds, enabled_flag):
    while enabled_flag:
        my_batch_action()
        time.sleep(interval_seconds)

if __name__ == "__main__":
    interval_seconds = 6  # Adjust this based on your desired interval
    job_enabled = True  # Set this flag to True to enable the job

    run_batch_job(interval_seconds, job_enabled)