#file uses old format before update
#Create a Bucket
import logging
import boto3

s3 = boto3.client('s3')
response = s3.create_bucket(bucket="Bucket_Name")


#def create_bucket('SheridanDevOps','us-east-1'):
#ACL = "public-read",
#CreateBucketConfiguration={
    #"LocationConstraint":"us-east-1"
    #}
#)

# Retrieve the list of existing buckets
import boto3
s3 = boto3.client('s3')
response = s3.list_buckets()

# Output the bucket names
import boto3
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


#how to delete from s3
import boto3
s3 = boto3.client('s3')
response = s3.delete_bucket(bucket='Bucket_Name')
    Key=('Key_Name.png')
