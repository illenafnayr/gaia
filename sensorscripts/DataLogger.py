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
                sensor_instance = self.sensorLogger()
                # timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row = sensor_instance.writeRow()
                csv_writer.writerow(row)

        except KeyboardInterrupt:
            print("ctrl + c:")