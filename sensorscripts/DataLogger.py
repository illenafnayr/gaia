# import csv
# import os
# from datetime import datetime, timedelta

# class DataLogger:
#     def __init__(self, sensorLogger, csv_file_path, header):
#         self.sensorLogger = sensorLogger
#         self.csv_file_path = csv_file_path
#         self.header = header

#         # Check if the CSV file exists
#         file_exists = os.path.isfile(self.csv_file_path)

#         # If the file doesn't exist, or if it exists but doesn't contain the specified headers,
#         # write the headers and fill the columns with zeros for the first row
#         if not file_exists or not self.are_headers_present():
#             self.initialize_csv_file()

#     def initialize_csv_file(self):
#         with open(self.csv_file_path, mode='a+', newline='') as csvfile:
#             csv_reader = csv.reader(csvfile)
#             csv_writer = csv.writer(csvfile)

#             # Check if the CSV file is empty
#             file_empty = not any(row for row in csv_reader)

#             # If the file is empty, write the headers and fill the columns with zeros for the first row
#             if file_empty or not self.are_headers_present():
#                 # Write the headers if they don't exist
#                 if not self.are_headers_present():
#                     csv_writer.writerow(self.header)


#     def are_headers_present(self):
#         # Check if the CSV file contains all the specified headers
#         with open(self.csv_file_path, 'r') as csvfile:
#             csv_reader = csv.reader(csvfile)
#             existing_headers = next(csv_reader, None)

#             # Exclude the "Timestamp" column from the comparison
#             return existing_headers is not None and all(header in existing_headers[1:] for header in self.header[1:])


#     def log_sensor_data(self):
#         try:
#             with open(self.csv_file_path, mode='a', newline='') as csvfile:
#                 csv_writer = csv.writer(csvfile)
#                 sensor_instance = self.sensorLogger()

#                 # Set headers based on the sensor instance
#                 self.set_headers(csv_writer, sensor_instance)

#                 row = sensor_instance.writeRow()

#                 # Inserting the current timestamp into the row
#                 timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#                 row.insert(0, timestamp)  # Assuming you want to insert the timestamp at the beginning of the row

#                 csv_writer.writerow(row)
#         except Exception as e:
#             print("Error logging sensor data: {}".format(e))

#     def set_headers(self, csv_writer, sensor_instance):
#         # Set headers based on the sensor instance
#         if not self.timestamp_logged:
#             header_row = ['Timestamp'] + sensor_instance.getHeaders()  # Assuming getHeaders returns the existing header
#             csv_writer.writerow(header_row)
#             self.timestamp_logged = True
#         else:
#             # Print only the "Timestamp" header for subsequent log entries
#             csv_writer.writerow(['Timestamp'])

import csv
from collections import OrderedDict
from datetime import datetime

class DataLogger:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.headers = self.get_headers()
        self.data = self.read_csv()

    def get_headers(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                headers = next(reader, [])
        except FileNotFoundError:
            headers = []
        return headers

    def read_csv(self):
        data = OrderedDict()
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    timestamp = row['timestamp']
                    data[timestamp] = row
        except FileNotFoundError:
            pass
        return data

    def add_data(self, new_data):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if not self.headers:
            self.headers = ['timestamp']
        for key in new_data.keys():
            if key not in self.headers:
                self.headers.append(key)
                # Add the new header to existing rows with a value of 0
                for timestamp, row in self.data.items():
                    row[key] = '0'
        self.data[timestamp] = new_data

    def save_to_csv(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            # Write header row
            writer.writeheader()
            # Write data rows
            writer.writerows(self.data.values())

# Example usage:
csv_file_path = 'your_data.csv'
logger = DataLogger(csv_file_path)

new_data1 = {'timestamp': '2023-11-16 12:00:00', 'header1': 'value1', 'header2': 'value2'}
new_data2 = {'timestamp': '2023-11-16 13:00:00', 'header2': 'value3', 'header3': 'value4'}

logger.add_data(new_data1)
logger.add_data(new_data2)

logger.save_to_csv()
