from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr




def queryDate(year):
    dynamodb = boto3.resource('dynamodb',  region_name='us-east-1', )
    table = dynamodb.Table('Movies')
    
    response = table.query(
        IndexName='rating-title-index',
        KeyConditionExpression=Key('title').eq(year)
    )
    
    for i in response['Items']:
        print(i['year'], ":", i['title'])

year = 'Pulp Fiction'
queryDate(year)