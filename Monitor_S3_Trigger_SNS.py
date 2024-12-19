import boto3
import os

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns')
    
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # SNS Topic ARN (replace with your ARN)
    sns_topic_arn = "arn:aws:sns:us-east-1:123456789012:my-sns-topic"
    
    message = f"New file uploaded to S3 bucket '{bucket_name}': {file_key}"
    print(message)
    
    # Publish notification to SNS
    sns.publish(TopicArn=sns_topic_arn, Message=message, Subject="S3 File Upload")
    return {"status": "Notification Sent"}
