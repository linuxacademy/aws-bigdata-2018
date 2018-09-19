from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


tableName = 'movies'
secondaryIndex = 'uploaded-rating-index'
partKey = 'uploaded'
pkValue = 'no'
rating = 7

def queryAdded(tableName, secondaryIndex, partkey, pkValue, rating):
    dynamodb = boto3.resource('dynamodb',  region_name='us-east-1', )
    table = dynamodb.Table('Movies')
    
    response = table.query(
        IndexName=secondaryIndex,
        KeyConditionExpression=Key(partKey).eq(pkValue) & Key('rating').gt(rating)        
    )
    
    return response
    
response = queryAdded(tableName, secondaryIndex, partkey, pkValue, rating)

for i in response['Items']:
    print(i['rating'], ":", i['title'])