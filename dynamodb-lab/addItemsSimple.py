from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb = boto3.resource('dynamodb',  region_name='us-east-1')
table = dynamodb.Table('movies')
table.put_item(
    Item={
        'year': 2005,
        'title': 'Batman Begins',
        'actor': 'Christian Bale'
    }
)
table.put_item(
    Item={
        'year': 2008,
        'title': 'The Dark Knight Rises',
        'actor': 'Christian Bale'
    }
)
table.put_item(
    Item={
        'year': 2008,
        'title': 'Tropic Thunder',
        'actor': 'Robert Downey Jr.'
    }
)
table.put_item(
    Item={
        'year': 2008,
        'title': 'Iron Man',
        'actor': 'Robert Downey Jr.'
    }
)

response = table.scan()

for i in response['Items']:
    print("added item:", i['year'], ":", i['title'], ":", i['actor'])