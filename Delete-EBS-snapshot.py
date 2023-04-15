#delete EBS snapshot
import boto3

ebs = boto3.resource('ebs')
response = ebs.delete_snapshot(
    SnapshotId='snap-1234567890abcdef0',
)

print(response)