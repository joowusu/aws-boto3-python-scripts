#!/usr/bin/env python3.7

"""
A python script that creates a S3 bucket.
"""

import boto3

client = boto3.client('s3')

response = client.create_bucket(
    #ACL='public-read',  # The bucket is public.
    ACL='private',       # The bucket is not public.
    Bucket='luitkura-bucket-boto3',  # Name of s3 bucket.
    CreateBucketConfiguration={
        'LocationConstraint': 'us-west-1'
    },   
)

print(response)
