import time
import sys
import os
import csv
from datetime import datetime  # Import the datetime module

libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_TSL2591 import TSL2591

logging.basicConfig(level=logging.INFO)

sensor = TSL2591.TSL2591()

csv_file_path = 'sensor_data.csv'

try:
    with open(csv_file_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Timestamp', 'Lux', 'Infrared', 'Visible', 'FullSpectrum'])

        while True:
            lux = sensor.Lux
            infrared = sensor.Read_Infrared
            visible = sensor.Read_Visible
            full_spectrum = sensor.Read_FullSpectrum

            # Get the current timestamp
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            row = [timestamp, lux, infrared, visible, full_spectrum]

            print('Timestamp: %s, Lux: %d, Infrared light: %d, Visible light: %d, Full spectrum (IR + visible) light: %d' % tuple(row))
            csv_writer.writerow(row)

            time.sleep(120)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    sensor.Disable()
    exit()
