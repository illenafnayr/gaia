# batch.py
import time
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from sensorscripts.DataLogger import DataLogger
from sensorscripts.TSL2591X.TSLX2591XDataLogger import LightSensorDataLogger

custom_header = ['Timestamp', 'Lux', 'Infrared', 'Visible', 'FullSpectrum']
logger = DataLogger(LightSensorDataLogger, csv_file_path='light-sensor-data.csv', header=custom_header)
logger.log_sensor_data()
time.sleep(5)
logger.log_sensor_data()
time.sleep(5)
logger.log_sensor_data()
time.sleep(5)
logger.log_sensor_data()