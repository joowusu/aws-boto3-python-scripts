#!/usr/bin/env python3.7S

"""
A Python script that uses boto3 to scan a DynamoDB table.
By Joan Owusu
"""

import boto3  # Python SDK that allows the interaction with DynamoDB APIs.

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')  # Instantiate the AWS DynamoDB resource.
from boto3.dynamodb.conditions import Key, Attr  #  Allows the scanning and querying of tables based on conditions related to key and attributes.  

table = dynamodb.Table('Critical_Care_Unit_Patients')  # Assigns name of the DynamoDB table to a variable "table."

# 
response = table.scan() # Scans the entire table and assign the resutls to the response variable in a dictionary form. 
 
#  A forloop that prints the table infomation stored in the response variable. 
print()
print("List of items in the table.")
for item in response['Items']:   
    print(item)
    print()
    
# Scans for patient/patients whose PATIENT-ID begins with '8' 
print()
print("Patient/Patients whose PATIENT-ID begins with '8")
response = table.scan(FilterExpression=Attr('Patient-ID').begins_with('8'))
items = response['Items']
print(items)
print()

# Scans for patient/patients whose Date-Of-Birth contains '1970'
print()
print("Patient/Patients whose Date of Birth contains '1970'")
response = table.scan(FilterExpression=Attr('Date-Of-Birth').contains('1970'))
items = response['Items']
print(items)