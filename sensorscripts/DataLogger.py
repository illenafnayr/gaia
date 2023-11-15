import csv
from TSL2591X.TSLX2591XDataLogger import LightSensorDataLogger

class DataLogger:
    def __init__(self, sensorLogger, csv_file_path, header=['Timestamp', 'Lux', 'Infrared', 'Visible', 'FullSpectrum']):
        self.sensorLogger = sensorLogger
        self.csv_file_path = csv_file_path
        self.header = header

        # Create the CSV file and write the header if it doesn't exist
        with open(self.csv_file_path, mode='a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(self.header)

    def log_sensor_data(self):
        try:
            with open(self.csv_file_path, mode='a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                # Get the current timestamp
                # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Create a row of sensor data
                row = self.sensorLogger().writeRow()

                # Log the data to the CSV file
                csv_writer.writerow(row)

                print('Timestamp: %s, Lux: %d, Infrared light: %d, Visible light: %d, Full spectrum (IR + visible) light: %d' % tuple(row))

        except KeyboardInterrupt:
            print("ctrl + c:")
            # Handle any necessary cleanup or logging when KeyboardInterrupt occurs

# Example usage:
# Assuming the SensorDataLogger is initialized somewhere in your main script
# and you have sensor data to log
# lux_value = 100  # Replace with actual Lux value
# infrared_value = 50  # Replace with actual Infrared value
# visible_value = 75  # Replace with actual Visible value
# full_spectrum_value = 125  # Replace with actual FullSpectrum value

# Dynamic CSV file path and header
# custom_csv_file_path = 'custom_sensor_data.csv'
custom_header = ['Timestamp', 'Lux', 'Infrared', 'Visible', 'FullSpectrum']

# Create an instance of the SensorDataLogger with dynamic parameters
logger = DataLogger(LightSensorDataLogger, csv_file_path='ligh-sensor-data.csv', header=custom_header)
