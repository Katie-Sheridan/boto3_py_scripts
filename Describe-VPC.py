#describe vpc

import boto3
vpc =  
response = client.describe_vpcs(
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