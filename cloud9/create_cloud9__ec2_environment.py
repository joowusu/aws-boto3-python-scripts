#!/usr/bin/env python3.7

"""
A python script that creates a cloud9 ec2 enviroment.
"""

import boto3
import uuid # Generates a ramdom universally unique identifier / unique name for EC2 instance. 

client = boto3.client('cloud9')

response = client.create_environment_ec2(
    name=str(uuid.uuid4()), # Generate a ramond name.
    instanceType='t2.micro',
    imageId='amazonlinux-2-x86_64', # Amazon Linux 2
)

print(response)
