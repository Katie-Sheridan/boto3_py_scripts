import boto3

response = client.terminate_instances(
    InstanceIds=[
        'string',
    ],
    DryRun=True|False
)