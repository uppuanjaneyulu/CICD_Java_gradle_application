import boto3
import boto3


client = boto3.client('ec2',aws_access_key_id='AKIA2QEFLENzzzzCE5S',
    aws_secret_access_key='F7GXkGPyi0Lsj7S99D8gSmjIXHznsssssBDNDN',
    region_name='us-east-1')


vpc = client.describe_vpcs()
for keys in vpc['Vpcs']:
    print(keys['CidrBlock'],'-->',keys['VpcId'])


nums = client.describe_instances()
mantags = ["Env","CostCenter","Email","Name"]
for items in nums['Reservations']:
        for holes in items['Instances']:
            for mytags in holes['Tags']:
                if mytags["Key"] in mantags:
                    print ("Tag",mytags["Key"],"Exists.")
                else:
                    print("Lets shutdown ",holes['InstanceId'])


for items in nums['Reservations']:
        for holes in items['Instances']:
            for mytags in holes['Tags']:
                if mytags["Key"] in mantags:
                    print ("Tag",mytags["Key"],"Exists.")
                else:
                    print("Lets shutdown ",holes['InstanceId'])


#BUG
this-email-bug@gmail.com


#Code Smell
#https://towardsdatascience.com/5-python-code-smells-you-should-be-wary-of-c48cc0eb9d8b
def addElements(a=[]):
    a.append(5)
    return aaddElements()
# [5]
addElements()
# [5, 5]
