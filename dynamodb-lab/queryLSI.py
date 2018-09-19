from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr



tableName = 'movies'
secondaryIndex = 'year-actor-index'
pk = 2005
attrib = 'year'

def queryLSI(tableName, indexName, pk, attrib):
    dynamodb = boto3.resource('dynamodb',  region_name='us-east-1')
    table = dynamodb.Table(tableName)
    
    response = table.query(
        IndexName= secondaryIndex,
        KeyConditionExpression=Key('year').eq(pk) #& Key('actor').between('A', 'D')
    )
    return response

response = queryLSI(tableName, secondaryIndex, pk, attrib)

for i in response['Items']:
    print(i['year'], ":", i['title'], ":", i['actor'])