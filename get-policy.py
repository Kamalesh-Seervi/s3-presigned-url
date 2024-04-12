import boto3
from botocore.client import Config
import os

# Retrieving access keys from environment variables
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# AWS region
region = "eu-central-1"

# S3 bucket and object key
bucket_name = "your_bucket_name"
object_key = "your_object_key"

# Creating an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4'),
    region_name=region,
)

# Generate presigned URL for GET
presigned_url = s3_client.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_key},
    ExpiresIn=3600  # Expiration time in seconds (e.g., 1 hour)
)

print("Presigned URL for GET:", presigned_url)
