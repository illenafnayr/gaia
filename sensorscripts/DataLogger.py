import csv
from collections import OrderedDict
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
                writer.writerow(headers)
        return headers

    def read_csv(self):
        data = OrderedDict()
        try:
            with open(self.csv_file, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data[row['timestamp']] = row
        except FileNotFoundError:
            pass
        return data

    def add_data(self):
        new_data = self.sensor_logger.writeRow()

        # If headers are not set, use the headers from sensor_logger
        # Convert new_data to a list of strings
        new_data_strings = [str(item) for item in new_data]

        # Create a new row dictionary
        new_row = dict(zip(self.headers, new_data_strings))
        print(new_row)

        # Append the new row to the data dictionary
        self.data[len(self.data) + 1] = new_row  # Using a numeric key instead of timestamp

        # Save to CSV without using with block
        self.save_to_csv()

    def save_to_csv(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write header row
            header_row = self.headers
            writer.writerow(header_row)

            # Write data rows
            for _, row in self.data.items():
                # Extract values including a default value for missing keys
                values = [row.get(key, '') for key in self.headers]
                # Write the row
                writer.writerow(values)

    def add_timestamp(self, timestamp):
            for key, row in self.data.items():
                if isinstance(row, dict):
                    row['timestamp'] = timestamp
                else:
                    print(f"Warning: Unexpected data format for key {key}: {row}")