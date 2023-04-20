#!/usr/bin/env python3.7

"""
A python script that uploads multiple files to s3 using boto3
"""

import boto3
import os
import glob  # Return all file paths that match a specific pattern.

files = glob.glob('/tmp/*.txt')
print(files)

for file in files:
    s3_client = boto3.client('s3')
    s3_client.upload_file(
    Filename=file,
    Bucket="newjackcity1990",
    Key=file.split("/")[-1])
