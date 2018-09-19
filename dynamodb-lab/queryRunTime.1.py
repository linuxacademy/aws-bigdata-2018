from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd


# def queryDate(time):
def queryDate():
    dynamodb = boto3.resource('dynamodb',  region_name='us-east-1', )
    table = dynamodb.Table('Movies')
    
    response = table.scan(
        # IndexName='running_time-rating-index',
        # KeyConditionExpression=Key('running_time').eq(time)
    )
    
    data = []
    for i in response['Items']:
        data.append(i['rating'],i['title'],i['running_time'])
        return data

# queryDate(int(sys.argv[1]))
data = queryDate()
df = pd.DataFrame(columns=index)
df.append(data)
