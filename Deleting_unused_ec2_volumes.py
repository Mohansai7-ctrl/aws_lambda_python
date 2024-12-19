import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        print(f"Deleting unused volume: {volume_id}")
        ec2.delete_volume(VolumeId=volume_id)
    return {"status": "Cleanup Completed"}
