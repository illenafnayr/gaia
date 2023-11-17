import csv
from collections import OrderedDict
from datetime import datetime

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
            headers = self.sensor_logger.headers
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
    def add_data(self):
        new_data = self.sensor_logger.writeRow()
        
        # If headers are not set, use generic names like 'Column1', 'Column2', etc.
        if not self.headers:
            self.headers = [f'Column{i}' for i in range(1, len(new_data) + 1)]
        
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Convert new_data to a list of strings
        new_data_strings = [str(item) for item in new_data]
        
        # Create a new row dictionary
        new_row = {'timestamp': timestamp, **dict(zip(self.headers, new_data_strings))}
        
        # Append the new row to the data dictionary
        self.data[timestamp] = new_row
        
        self.save_to_csv()

    def save_to_csv(self):
        with open(self.csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=self.headers)
            # Write header row
            writer.writeheader()
            # Write data rows
            for timestamp, row in self.data.items():
                if isinstance(row, dict):
                    writer.writerow(row)
                else:
                    print(f"Warning: Unexpected data format for timestamp {timestamp}: {row}")

    def add_timestamp(self):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        for timestamp in self.data:
            if isinstance(self.data[timestamp], dict):
                self.data[timestamp]['timestamp'] = current_time
            else:
                print(f"Warning: Unexpected data format for timestamp {timestamp}: {self.data[timestamp]}")

