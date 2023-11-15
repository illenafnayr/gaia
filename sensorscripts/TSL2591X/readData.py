import boto3
import pandas as pd
from io import StringIO
import os

from dotenv import load_dotenv
load_dotenv()

secret_key_id = os.getenv('AWS_SECRET_ACCESS_KEY_ID')
secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

def read_merged_csv_from_s3(aws_access_key_id, aws_secret_access_key, aws_region, s3_bucket_name, s3_object_key):
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

    csv_content = s3.get_object(Bucket=s3_bucket_name, Key=s3_object_key)['Body'].read().decode('utf-8')

    df = pd.read_csv(StringIO(csv_content))

    return df

aws_access_key_id = secret_key_id
aws_secret_access_key = secret_key
aws_region = 'us-east-1'
s3_bucket_name = 'gaia-sensor-data'
s3_object_key = 'gaia-sensor-data-updated.csv'

merged_df = read_merged_csv_from_s3(aws_access_key_id, aws_secret_access_key, aws_region, s3_bucket_name, s3_object_key)

print(merged_df)