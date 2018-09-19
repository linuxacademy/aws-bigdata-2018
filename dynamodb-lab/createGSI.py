from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import sys
import random
from time import sleep
# from boto.dynamodb2 import table

dynamodb = boto3.resource('dynamodb',  region_name='us-east-1')
table = dynamodb.Table('Movies')
table.update(
    AttributeDefinitions = [
        {
            "AttributeName": "title", "AttributeType": 'S'
        },
        {
            "AttributeName": "rating", "AttributeType": 'N'
        }
    ],
    GlobalSecondaryIndexUpdates=[
        {
            'Create': {
                'IndexName': 'title-rating-index',
                'KeySchema': [
                    {
                        'AttributeName': 'title',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'rating',
                        'KeyType': 'RANGE'
                    }
                ],
                'Projection': {
                    'ProjectionType': 'ALL'
                },
                'ProvisionedThroughput': {
                    'ReadCapacityUnits': 1,
                    'WriteCapacityUnits': 1
                }
            }
        }
    ]
)