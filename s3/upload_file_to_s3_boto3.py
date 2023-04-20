#!/usr/bin/env python3.7

"""
A python script that uploads a file to s3 using boto3
"""

import boto3

s3_client = boto3.client('s3')

s3_client.upload_file(
    Filename="/tmp/hello.txt",
    Bucket="luitkura1-bucket-boto3",
    Key="hello.txt")