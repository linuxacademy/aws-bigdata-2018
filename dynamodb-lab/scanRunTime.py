from __future__ import print_function # Python 2/3 compatibility
import sys
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr
import pandas as pd



def queryDate():
    dynamodb = boto3.resource('dynamodb',  region_name='us-east-1', )
    table = dynamodb.Table('Movies')
    
    response = table.scan(
        IndexName='rating-title-index'
        )

    item_list = []
    for i in response['Items']:
        item = {'rating':i['rating'], 'title':i['actors'], 'running_time':i['running_time']}
        item_list.append(item)
    df = pd.DataFrame(data=item_list)
    return df.sort_values('rating')

data = queryDate()
print(data)

