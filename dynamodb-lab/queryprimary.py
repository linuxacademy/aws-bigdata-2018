from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr


def queryDate(year):
    dynamodb = boto3.resource('dynamodb',  region_name='us-east-1', )
    table = dynamodb.Table('movie')
    
    response = table.query(
        KeyConditionExpression=Key('year').eq(year)
    )
    
    for i in response['Items']:
        print(i['year'], ":", i['title'], ":", i['actors'], ":", i['rating'], ":", i['running_time'])

queryDate(int(sys.argv[1]))
