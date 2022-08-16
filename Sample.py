from distutils.command.clean import clean
from http import client
from msilib.schema import Error
import os
import boto3
from botocore.exceptions import ClientError  

access_key = "access_key"
access_secret = "secret_access_key"
bucket_name = "bucket_name"

#-- connecting to s3
try:
    client_s3 = boto3.client(
        's3',
        aws_access_key_id = access_key,
        aws_secret_access_key = access_secret 
    )

except Exception as e:
    print("An error occured while attempting to connect to AWS S3 Service: {}".format(e))

#-- upload files to S3 bucket
# data_file = os.path.join(os.getcwd()) --> path to be taken
for file in os.listdir('--path--'): #path name to be specified
    if not file.startswith('~'): 
        try:
            client_s3.upload_file(
                # os.path.join(), -- > path
                bucket_name,
                file
            )
        except ClientError as e:
            print("Incorrect Credential : {}".format(e))
        except Exception as e:
            print(e)

#-- Downloading file fromS3 bucket
# client_s3.download_file(bucket_name,file_name, name)--> logic to list filenames


    
