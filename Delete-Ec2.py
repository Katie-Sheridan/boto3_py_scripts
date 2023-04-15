import boto3
ec2 = boto3.resource('ec2')

response = ec2.stop_instance(
    InstanceIds=[
        'string',
    ],
    DryRun=True|False
)