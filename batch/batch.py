import time
from sensorscripts.DataLogger import DataLogger
from sensorscripts.TSL2591X.TSLX2591XDataLogger import LightSensorDataLogger

custom_header = ['Timestamp', 'Lux', 'Infrared', 'Visible', 'FullSpectrum']
logger = DataLogger(LightSensorDataLogger, csv_file_path='light-sensor-data.csv', header=custom_header)
logger.log_sensor_data()
time.sleep(3)
logger.log_sensor_data()
time.sleep(3)
logger.log_sensor_data()
time.sleep(3)
