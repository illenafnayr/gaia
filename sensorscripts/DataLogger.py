import csv
from collections import OrderedDict
from datetime import datetime
import logging

class DataLogger:
    def __init__(self, sensor_logger, csv_file):
        self.sensor_logger = sensor_logger
        self.csv_file = csv_file
        self.headers = self.get_headers()
        self.data = self.read_csv()

    def get_headers(self):
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                headers = next(reader, [])
        except FileNotFoundError:
            headers = self.sensor_logger.getHeaders()
            # Create an empty CSV file with headers
            with open(self.csv_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['timestamp', *headers])
        return headers
    
    def read_csv(self):
        data = OrderedDict()
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.reader(file)
                headers = next(reader, [])  # Read the header row
                if 'timestamp' not in headers:
                    logging.warning("No 'timestamp' column in the CSV file.")
                    return data

                for row in reader:
                    timestamp = row[headers.index('timestamp')]
                    data[timestamp] = OrderedDict(zip(headers, row))
        except FileNotFoundError:
            pass
        return data

    def add_data(self):
        new_sensor_readings = self.sensor_logger.writeRow()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # Add logic to get the timestamp, e.g., datetime.datetime.now()
        # Create a new row dictionary
        new_row = [timestamp, *new_sensor_readings]

        # Append the new row to the data dictionary
        self.data[timestamp] = OrderedDict(zip(self.headers, new_row))

        # Save to CSV without using with block
        self.save_to_csv()

    def save_to_csv(self):
        with open(self.csv_file, 'a', newline='') as file:
            writer = csv.writer(file)

            # Write data rows
            for _, row in self.data.items():
                # Write the row directly if it's a list
                if isinstance(row, list):
                    writer.writerow(row)
                elif isinstance(row, dict):
                    # Extract values including a default value for missing keys
                    values = [row.get(key, '') for key in self.headers]
                    # Write the row
                    writer.writerow(values)
                    print(values)
                else:
                    print(f"Warning: Unexpected data format for key {key}: {row}")

    def add_timestamp(self, timestamp):
        for key, row in self.data.items():
            if isinstance(row, dict):
                row['timestamp'] = timestamp
            else:
                print(f"Warning: Unexpected data format for key {key}: {row}")
