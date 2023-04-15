#list EBS snapshot

import boto3
ebs = boto3.client('ebs')

response = ebs.describe_snapshots(
    Filters=[
        {
            'Name': 'string',
            'Values': [
                'string',
            ]
        },
    ],
    MaxResults=123,
    NextToken='string',
    OwnerIds=[
        'string',
    ],
    RestorableByUserIds=[
        'string',
    ],
    SnapshotIds=[
        'string',
    ],
    DryRun=True|False
)