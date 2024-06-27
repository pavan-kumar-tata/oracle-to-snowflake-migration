import boto3
from datetime import datetime
import os

def s3Client():
    """
    Create an S3 client using AWS credentials.
    onfigure AWS credentials using environment variables or IAM roles
    AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY securely.
    """
    # Initialize the S3 client
    s3 = boto3.client('s3')
    return s3

def upload_directory_to_s3(directory, bucket_name, prefix=''):
    """
    Upload the contents of a local directory to an S3 bucket.
    
    Parameters:
    directory (str): Path to the local directory.
    bucket_name (str): Name of the S3 bucket.
    prefix (str): S3 folder prefix where files will be uploaded.
    """
    s3_client = s3Client()
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            local_path = os.path.join(root, file)  # Full local path of the file
            s3_path = os.path.join(prefix, os.path.relpath(local_path, directory))  # S3 path for the file
            
            # Read and print data before uploading
            with open(local_path, 'r') as file_data:
                data = file_data.read()
                print(f"Uploading data to S3: {s3_path}")
                print(f"Data: {data[:500]}...")  # Print the first 500 characters to avoid too much output
            
            # Upload file to S3
            s3_client.upload_file(local_path, bucket_name, s3_path)

if __name__ == "__main__":
    # Specify your local path for your main folder
    local_directory = ''  # e.g., '/path/to/your/local/directory'
    bucket_name = ''  # e.g., 'your-s3-bucket-name'
    
    # Name of the main folder in S3
    prefix = 'housing_data_set'
    
    # Upload the directory to S3
    upload_directory_to_s3(local_directory, bucket_name, prefix)
