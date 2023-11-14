import pandas as pd
import boto3
from io import StringIO

# AWS credentials and S3 bucket information
aws_access_key_id = ''
aws_secret_access_key = ''
# aws_access_key_id = 'your_access_key_id'
# aws_secret_access_key = 'your_secret_access_key'
aws_region = 'us-east-1'
s3_bucket_name = 'gaia-sensor-data'
s3_object_key1 = 'gaia-sensor-data.csv'  # Update with the correct S3 object key

# Connect to S3
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Download CSV file from S3
csv_content1 = s3.get_object(Bucket=s3_bucket_name, Key=s3_object_key1)['Body'].read().decode('utf-8')
csv_content2 = "./sensor_data.csv"

# Read CSV content into Pandas DataFrames
df1 = pd.read_csv(StringIO(csv_content1))
df2 = pd.read_csv(StringIO(csv_content2))

# Perform an inner join on the common column(s)
# Replace "common_column" with the actual common column name(s) in your CSV files
# If there are multiple common columns, pass them as a list, e.g., on=['common_column1', 'common_column2']
result_df = pd.merge(df1, df2, on=['Timestamp','Lux','Infrared','Visible','Full Spectrum'], how='inner')

# Save the result to a new CSV file
result_csv_content = result_df.to_csv(index=False)

# Upload the updated CSV file to S3
result_s3_object_key = 'gaia-sensor-data.csv'  # Update with the desired S3 object key
s3.put_object(Body=result_csv_content, Bucket=s3_bucket_name, Key=result_s3_object_key)

print(f"Join successful. Result saved to S3 bucket with key: {result_s3_object_key}")
