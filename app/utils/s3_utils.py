import boto3
import os

# AWS S3 configuration
s3 = boto3.client(
    's3',
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
)

def upload_to_s3(paragraphs):
    # Function to upload paragraphs to S3
    # You need to implement this function
    # Example implementation:
    bucket_name = 'your_bucket_name'
    for i, paragraph in enumerate(paragraphs):
        folder_name = f'folder_{i + 1}'  # Adjust folder naming as per your requirements
        key = f'{folder_name}/paragraph_{i + 1}.txt'
        s3.put_object(Bucket=bucket_name, Key=key, Body=paragraph)