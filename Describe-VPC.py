#describe vpc

import boto3
vpc = boto3.client('vpc') 

response = vpc.describe_vpcs(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    VpcIds=[
        'string',
    ],
    DryRun=True|False,
    NextToken='string',
    MaxResults=123
)