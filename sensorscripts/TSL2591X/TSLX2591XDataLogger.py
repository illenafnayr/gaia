from datetime import datetime  # Import the datetime module
import logging

from TSL2591 import TSL2591

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
