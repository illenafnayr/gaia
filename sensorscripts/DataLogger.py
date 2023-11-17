import csv
import os
from datetime import datetime, timedelta

class DataLogger:
    def __init__(self, sensorLogger, csv_file_path, header):
        self.sensorLogger = sensorLogger
        self.csv_file_path = csv_file_path
        self.header = header
        self.timestamp_logged = False  # Initialize timestamp_logged attribute

        # Check if the CSV file exists
        file_exists = os.path.isfile(self.csv_file_path)

        # If the file doesn't exist, or if it exists but doesn't contain the specified headers,
        # write the headers and update the existing rows with zeros until the current timestamp
        if not file_exists or not self.are_headers_present():
            self.initialize_csv_file()

    def initialize_csv_file(self):
        with open(self.csv_file_path, mode='a+', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            existing_headers = next(csv_reader, None)

            # Write the headers if they don't exist
            if not existing_headers:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(self.header)

            # Update existing rows with zeros until the current timestamp
            current_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            zero_row = [0] * len(self.header)
            zero_row[0] = "Timestamp"

            for row in csv_reader:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(zero_row)
                if row[0] == current_timestamp:
                    break

    def are_headers_present(self):
        # Check if the CSV file contains all the specified headers
        with open(self.csv_file_path, 'r') as csvfile:
            csv_reader = csv.reader(csvfile)
            existing_headers = next(csv_reader, None)

            # Exclude the "Timestamp" column from the comparison
            return existing_headers is not None and all(header in existing_headers[1:] for header in self.header[1:])

    def log_sensor_data(self):
        try:
            with open(self.csv_file_path, mode='a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                sensor_instance = self.sensorLogger()
                row = sensor_instance.writeRow()

                # Inserting the current timestamp into the row
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                row.insert(0, timestamp)  # Assuming you want to insert the timestamp at the beginning of the row

                # Adding a header for the timestamp column if not already present
                if not self.timestamp_logged:
                    header_row = ['Timestamp'] + sensor_instance.getHeaders()  # Assuming getHeader returns the existing header
                    csv_writer.writerow(header_row)
                    self.timestamp_logged = True

                csv_writer.writerow(row)
        except Exception as e:
            print("Error logging sensor data: {}".format(e))
