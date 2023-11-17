from datetime import datetime
import logging
from sensorscripts.TSL2591X.TSL2591 import TSL2591

logging.basicConfig(level=logging.INFO)

class LightSensorDataLogger:
    def __init__(self, headers=['Lux', 'Infrared', 'Visible', 'Full Spectrum']):
        self.headers = headers

    def writeRow(self):
        sensor = TSL2591()
        lux = sensor.Lux
        infrared = sensor.Read_Infrared
        visible = sensor.Read_Visible
        full_spectrum = sensor.Read_FullSpectrum

        row = [lux, infrared, visible, full_spectrum]
        # print('Lux: %d, Infrared light: %d, Visible light: %d, Full spectrum (IR + visible) light: %d' % tuple(row))

        sensor.Disable()
        return row

    def getHeaders(self):
        return self.headers
