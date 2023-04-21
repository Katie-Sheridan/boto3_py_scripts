import boto3

# Create SQS client
sqs = boto3.client('sqs')

# Create a SQS queue
response = sqs.create_queue(
    QueueName='Shipping-SQS',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)

# Get URL for SQS queue
response = sqs.get_queue_url(QueueName='Shipping-SQS')

print(response['QueueUrl'])
