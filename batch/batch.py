# batch.py
import time
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from sensorscripts.DataLogger import DataLogger
from sensorscripts.TSL2591X.TSLX2591XDataLogger import LightSensorDataLogger


def run_batch_job(interval_seconds, enabled_flag):
    while enabled_flag:

        lightSensor = LightSensorDataLogger
        get_sensor_readings(lightSensor)
        time.sleep(interval_seconds)
def get_sensor_readings(SensorDataLogger):
        logger = DataLogger(SensorDataLogger, csv_file_path='light-sensor-data.csv', header=SensorDataLogger.getHeaders())
        logger.log_sensor_data()

if __name__ == "__main__":
    interval_seconds = 6  # Adjust this based on your desired interval
    job_enabled = True  # Set this flag to True to enable the job

    run_batch_job(interval_seconds, job_enabled)