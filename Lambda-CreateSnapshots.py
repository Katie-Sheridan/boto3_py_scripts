#create lambda snapshots
from datetime import datetime

import boto3

def lambda_handler(event, context):
    ec2_client = boto3.client('ec2')