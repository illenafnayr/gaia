import csv
import os
from datetime import datetime

class DataLogger:
    def __init__(self, sensorLogger, csv_file_path, header=['Timestamp', 'Lux', 'Infrared', 'Visible', 'FullSpectrum']):
        self.sensorLogger = sensorLogger
        self.csv_file_path = csv_file_path
        self.header = header

        # Check if the CSV file exists
        file_exists = os.path.isfile(self.csv_file_path)

        # If the file doesn't exist, or if it exists but doesn't contain the specified headers,
        # write the headers and fill the columns with zeros until the current timestamp
        if not file_exists or not self.are_headers_present():
            with open(self.csv_file_path, mode='a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)

                # Write the headers if they don't exist
                if not file_exists:
                    csv_writer.writerow(self.header)

                # Fill columns with zeros until the current timestamp
                if not file_exists:
                    current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    zero_row = [0] * len(self.header)
                    while True:
                        zero_row[0] = current_timestamp
                        csv_writer.writerow(zero_row)
                        current_timestamp = (datetime.strptime(current_timestamp, '%Y-%m-%d %H:%M:%S') +
                                            timedelta(minutes=1)).strftime('%Y-%m-%d %H:%M:%S')
                        if current_timestamp > datetime.now().strftime('%Y-%m-%d %H:%M:%S'):
                            break

    def are_headers_present(self):
        # Check if the CSV file contains all the specified headers
        with open(self.csv_file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            existing_headers = next(csv_reader, None)

            # Check if all headers in self.header are present in existing_headers
            return all(header in existing_headers for header in self.header)

    def log_sensor_data(self):
        try:
            with open(self.csv_file_path, mode='a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                sensor_instance = self.sensorLogger()
                row = sensor_instance.writeRow()
                csv_writer.writerow(row)

        except KeyboardInterrupt:
            print("ctrl + c:")
