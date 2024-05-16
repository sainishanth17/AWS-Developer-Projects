import boto3
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
access_key = config['aws_credentials']['accesskey']
secret_key = config['aws_credentials']['secretkey']

s3client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

bucket_response = s3client.list_buckets()

bucket_list = list(map(lambda x:x["Name"], bucket_response["Buckets"]))

for bucket in bucket_list:
    print(bucket)
