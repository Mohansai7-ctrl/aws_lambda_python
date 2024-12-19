import boto3

def lambda_handler(event, context):
    iam = boto3.client('iam')
    user_name = 'devops-user'  # Replace with IAM username
    
    # List access keys
    keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']
    
    for key in keys:
        access_key_id = key['AccessKeyId']
        print(f"Deleting old access key: {access_key_id}")
        iam.delete_access_key(UserName=user_name, AccessKeyId=access_key_id)
    
    # Create new access key
    new_key = iam.create_access_key(UserName=user_name)['AccessKey']
    print(f"New Access Key: {new_key['AccessKeyId']}")
    return {"status": "Key Rotated", "NewAccessKey": new_key['AccessKeyId']}
