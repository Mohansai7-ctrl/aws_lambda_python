import boto3
from datetime import datetime, timedelta

def lambda_handler(event, context):
    region = 'us-east-1'
    retention_days = 7  # Define retention period
    ec2 = boto3.client('ec2', region_name=region)
    
    # Calculate deletion threshold date
    deletion_date = datetime.utcnow() - timedelta(days=retention_days)
    
    # Get all snapshots
    snapshots = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    for snapshot in snapshots:
        snapshot_date = snapshot['StartTime'].replace(tzinfo=None)
        if snapshot_date < deletion_date:
            print(f"Deleting snapshot {snapshot['SnapshotId']} from {snapshot_date}")
            ec2.delete_snapshot(SnapshotId=snapshot['SnapshotId'])
    return {"status": "Cleanup Completed"}
