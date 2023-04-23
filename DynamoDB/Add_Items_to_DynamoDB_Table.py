#!/usr/bin/env python3.7

"""
A Python script that uses Boto3 to add items to a DynamoDB table.
By Joan Owusu
"""

import boto3  # Python SDK that allows the interaction with DynamoDB APIs.

dynamodb = boto3.resource('dynamodb', region_name='us-east-1') #  Resource object offers higher level APIs.
table = dynamodb.Table('Critical_Care_Unit_Patients')

#  Create input objects as independent python dictionary objects.
item_1 = {"Patient-ID":"9894569827", "Date-Of-Birth":"1-24-1969"} 
item_2 = {"Patient-ID":"9897627163", "Date-Of-Birth":"10-12-1970"}
item_3 = {"Patient-ID":"2669433782", "Date-Of-Birth":"12-12-1966"}
item_4 = {"Patient-ID":"9051066650", "Date-Of-Birth":"6-7-1988"}
item_5 = {"Patient-ID":"2668337669", "Date-Of-Birth":"11-14-1956"}
item_6 = {"Patient-ID":"2475236917", "Date-Of-Birth":"4-48-1990"}
item_7 = {"Patient-ID":"3199713971", "Date-Of-Birth":"2-28-1945"}
item_8 = {"Patient-ID":"8461147610", "Date-Of-Birth":"3-5-1977"}
item_9 = {"Patient-ID":"7425640530", "Date-Of-Birth":"11-29-1989"}
item_10 = {"Patient-ID":"8465114654", "Date-Of-Birth":"9-25-1986"}
item_11 = {"Patient-ID":"8379781188", "Date-Of-Birth":"7-23-1958"}

# Items will be added at once using a batch_writer.
# A batch_writer is a high level helper object that handles adding and deleting items from DynamoDB in batch.

items_to_add = [item_1, item_2, item_3, item_4, item_5, item_6, item_7, item_8, item_9, item_10, item_11]  #  List of items to pass to the batch_writer.

with table.batch_writer() as batch:  #  Using batch object’s put_item method for every item in the list.
    for item in items_to_add:        #  batch_writer combines multiple "putitem" requests into a single "BatchWriteItem" API call to make to AWS.
        response = batch.put_item(Item={
            "Patient-ID": item["Patient-ID"],
            "Date-Of-Birth": item["Date-Of-Birth"]
        })