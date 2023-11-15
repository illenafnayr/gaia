import sys
import os
from datetime import datetime  # Import the datetime module

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)
import logging
from waveshare_TSL2591 import TSL2591

logging.basicConfig(level=logging.INFO)

sensor = TSL2591.TSL2591()

csv_file_path = 'TSL2591X_sensor_data.csv'

class LightSensorDataLogger:
    def writeRow(self):
        with open(csv_file_path, mode='w', newline='') as csvfile:
            lux = sensor.Lux
            infrared = sensor.Read_Infrared
            visible = sensor.Read_Visible
            full_spectrum = sensor.Read_FullSpectrum
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            row = [timestamp, lux, infrared, visible, full_spectrum]
            print('Timestamp: %s, Lux: %d, Infrared light: %d, Visible light: %d, Full spectrum (IR + visible) light: %d' % tuple(row))
            
            sensor.Disable()
            return row
