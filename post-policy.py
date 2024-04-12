import os
import boto3
from botocore.client import Config
import requests

# Informing the user about the requirement to create an AWS IAM account
print("Please ensure you have created an AWS IAM account and generated access keys.")

# Retrieving access keys from environment variables
ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")

# AWS region
region = "eu-central-1"

# Creating an S3 client
s3_client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    config=Config(signature_version='s3v4'),
    region_name=region,
)

# Define bucket name and prefix
bucket_name = "testjorzel"
prefix = "mytest/"

# Define object name using prefix and filename
object_name = prefix + "${filename}"

# Define expiration time for the presigned URL in seconds (e.g., 60 seconds)
expiration = 60

# Generate presigned POST URL
presigned_post = s3_client.generate_presigned_post(
    bucket_name,
    object_name,
    Fields=None,
    Conditions=[["starts-with", "$key", prefix]],
    ExpiresIn=expiration,
)

# Print the presigned POST URL
print("Presigned POST URL:")
print(presigned_post)
