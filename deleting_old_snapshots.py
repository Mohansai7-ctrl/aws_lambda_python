import boto3
import json
from datetime import datetime, timedelta

def lambda_handler(event, context):
    region = 'us-east-1'
    retention_days = 7
    ec2 = boto3.client('ec2', region_name=region)


    deletion_date = datetime.utcnow() - timedelta(days=retention_days)

    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']

    for snapshot in snapshots:
        snapshot_date < deletion_date
        


