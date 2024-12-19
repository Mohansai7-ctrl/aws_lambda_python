import boto3

def lambda_handler(event, context):
    logs = boto3.client('logs', region_name='us-east-1')
    log_group_name = '/aws/lambda/my-lambda-function'
    
    # Get the latest log stream
    streams = logs.describe_log_streams(logGroupName=log_group_name, orderBy='LastEventTime', descending=True)
    
    if streams['logStreams']:
        latest_stream = streams['logStreams'][0]
        print(f"Latest stream: {latest_stream['logStreamName']}")
    else:
        print("No log streams found.")
    return {"status": "Checked CloudWatch Logs"}
