import csv
import os
from datetime import datetime, timedelta

class DataLogger:
    def __init__(self, sensorLogger, csv_file_path, header):
        self.sensorLogger = sensorLogger
        self.csv_file_path = csv_file_path
        self.header = header

        # Check if the CSV file exists
        file_exists = os.path.isfile(self.csv_file_path)

        # If the file doesn't exist, or if it exists but doesn't contain the specified headers,
        # write the headers and fill the columns with zeros for the first row
        if not file_exists or not self.are_headers_present():
            self.initialize_csv_file()

    def initialize_csv_file(self):
        with open(self.csv_file_path, mode='a+', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            csv_writer = csv.writer(csvfile)

            # Check if the CSV file is empty
            file_empty = not any(row for row in csv_reader)

            # If the file is empty, write the headers and fill the columns with zeros for the first row
            if file_empty or not self.are_headers_present():
                # Write the headers if they don't exist
                if not self.are_headers_present():
                    csv_writer.writerow(self.header)


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

                print("row: {}", row)

                csv_writer.writerow(row)
        except Exception as e:
            print("Error logging sensor data: {}".format(e))
