import boto3
region = 'us-east-2'
instances = ['i-05be5c0c4039881ed']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))


import boto3
region = 'us-east-2'
instances = ['i-05be5c0c4039881ed']
ec2 = boto3.client('ec2', region_name=region)
def lambda_handler(event, context):
#    ec2.stop_instances(InstanceIds=instances)
    ec2.start_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))
