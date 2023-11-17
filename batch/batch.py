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
        get_sensor_reading(lightSensor)
        time.sleep(interval_seconds)

def get_sensor_reading(SensorDataLogger):
        sensor = SensorDataLogger()
        headers = sensor.getHeaders()
        print("headers: {}", headers)
        logger = DataLogger(SensorDataLogger, csv_file='light-sensor-data.csv')
        logger.add_data()
     
if __name__ == "__main__":
    interval_seconds = 3  # Adjust this based on your desired interval
    job_enabled = True  # Set this flag to True to enable the job

    run_batch_job(interval_seconds, job_enabled)