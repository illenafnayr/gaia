import csv
from collections import OrderedDict
from datetime import datetime

class DataLogger:
    def __init__(self, SensorLogger, csv_file):
        self.sensorLogger = SensorLogger()
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

    def add_data(self):
        new_data = self.sensorLogger.writeRow()
        if not self.headers:
            self.headers = [str(item) for item in new_data]
        for i, key in enumerate(self.headers):
            if key not in new_data:
                for _, row in self.data.items():
                    row[key] = '0'
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        # Convert new_data to a list of strings
        new_data_strings = [str(item) for item in new_data]
        
        new_data_with_timestamp = {'timestamp': timestamp, **dict(zip(self.headers, new_data_strings))}
        self.data.update(new_data_with_timestamp)
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
        # Ensure that each value in self.data is a dictionary
        self.data = {timestamp: {'timestamp': current_time, **data} for timestamp, data in self.data.items()}

