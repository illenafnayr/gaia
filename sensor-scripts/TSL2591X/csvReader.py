import pandas as pd
import os
import boto3
from io import StringIO
from dotenv import load_dotenv
load_dotenv()

secret_key_id = os.getenv('AWS_SECRET_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

aws_access_key_id = secret_key_id
aws_secret_access_key = secret_key
aws_region = 'us-east-1'
s3_bucket_name = 'gaia-sensor-data'
s3_object_key = 'gaia-sensor-data-updated.csv'
s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

try:
    csv_content = s3.get_object(Bucket=s3_bucket_name, Key=s3_object_key)['Body'].read().decode('utf-8')
    df1 = pd.read_csv(StringIO(csv_content))
except Exception as e:
    print(f"Error reading existing CSV from S3: {e}")
    df1 = pd.DataFrame()

local_csv_path = "./sensor_data.csv"
df2 = pd.read_csv(local_csv_path)

result_df = pd.concat([df1, df2], ignore_index=True)

result_csv_content = result_df.to_csv(index=False)

s3.put_object(Body=result_csv_content, Bucket=s3_bucket_name, Key=s3_object_key)

print(f"Update successful. Result saved to S3 bucket with key: {s3_object_key}")
