import boto3
import os

# AWS Lambda function to start/stop EC2 instances
def lambda_handler(event, context):
    region = 'us-east-1'  # Set the AWS region
    action = event.get('action', 'stop')  # Default action: stop
    ec2 = boto3.client('ec2', region_name=region)
    
    instances = ['i-1234567890abcdef0']  # Replace with your instance IDs
    
    if action == 'start':
        ec2.start_instances(InstanceIds=instances)
        print(f"Started instances: {instances}")
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instances)
        print(f"Stopped instances: {instances}")
    else:
        print(f"Invalid action: {action}")
    return {"status": "Success", "action": action}
