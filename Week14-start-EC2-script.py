# create Ec2 instances

import boto3
ec2 = boto3.resource('ec2')

# get 3 running development instances:
dev = ec2.create_instances(
    ImageId='ami-01a5f5bb7b408ee72',  #ami= my Cloud9 Ec2 AMI
    InstanceType='t2.micro',
    MaxCount= 3,
    MinCount= 3,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name','Value': 'Development'},
                {'Key': 'ENV','Value': 'Development'}
                ]
            }
        ]
    )

#create a production instance    
prod = ec2.create_instances(
    ImageId='ami-01a5f5bb7b408ee72',  #ami= my Cloud9 Ec2 AMI
    InstanceType='t2.micro',
    MaxCount= 1,
    MinCount= 1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {'Key': 'Name','Value': 'Production'},
                {'Key': 'ENV','Value': 'Production'}
                ]
            }
        ]
    )