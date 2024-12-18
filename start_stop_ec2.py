import json
import os
import boto3

def lamda_handler(event, context):
    region = 'us-east-1'
    action = event.get('action', 'stop')
    ec2 = boto3.client('ec2', region_name = region)

    instances = ['#instance_id']

    if action == 'start':
        ec2.start_instances(InstanceIds=instances)
        print(f"started these instances: {instances}")
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instances)
        print(f"stopped these instances: {instances}")
    else:
        print(f"invalid action: {instances}")

    return {
        "state"="success",
        "action"=action
    }