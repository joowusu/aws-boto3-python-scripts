#!/usr/bin/env python3.7

"""
A Python script that uses Boto3 to create a DynamoDB table.
"""

import boto3  # Import the boto3 module to have the ability to make calls to AWS APIs

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #  Instantiate the AWS DynamoDB resource.

# Create a DynamoDB Table "Critical_Care_Unit_Patients"
dynamodb_table = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Patient-ID', # Adds attribute "Patient-ID" to the table.
            'AttributeType': 'S',          # Attribute type is string. S = String, N = Number, B = Binary.
        },
        {
            'AttributeName': 'Date-Of-Birth', 
            'AttributeType': 'S',          
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'Patient-ID', # Adds Partition Key (primary key). 
            'KeyType': 'HASH',
        },
        {
            'AttributeName': 'Date-Of-Birth', # Adds Sort Key (attribute range).
            'KeyType': 'RANGE',
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5,
    },
    TableName='Critical_Care_Unit_Patients', # Creates table name.
)

print()
print(dynamodb_table)
print()
print("Table has been created successfully.")
print()
print("Table status:", dynamodb_table.table_status)  # Prints status of table if "resource API is used"