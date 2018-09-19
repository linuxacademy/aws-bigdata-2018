from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
import sys
import random
from time import sleep

dynamodb = boto3.resource('dynamodb',  region_name='us-east-1')


table = dynamodb.create_table(
   TableName='Movies',
   KeySchema=[
       {
           'AttributeName': 'title',
           'KeyType': 'HASH'  #Partition key
       },
       {
           'AttributeName': 'year',
           'KeyType': 'RANGE'  #Sort key
       }
   ],
   AttributeDefinitions=[
       {
           'AttributeName': 'title',
           'AttributeType': 'S'
       },
       {
           'AttributeName': 'year',
           'AttributeType': 'N'
       },

   ],
   ProvisionedThroughput={
       'ReadCapacityUnits': 1,
       'WriteCapacityUnits': 1
   }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='Movies')

table = dynamodb.Table('Movies')

choices = ['yes', 'no']
i = 0
# with open("/home/cloud_user/moviedata.json") as json_file:
with open("moviedata.json") as json_file:

    movies = json.load(json_file, parse_float = decimal.Decimal)
    for movie in movies:
        i = i + 1
        if i == 100:
            sys.exit()
        year = int(movie['year'])
        title = movie['title']
        star = movie['actors'][0]
        rating = movie['rating']
        running_time = movie['running_time_secs']
        uploaded = random.choice(choices)

        print("Adding movie:", year, title, star, rating, running_time, in_stock)

        table.put_item(
           Item={
               'year': year,
               'title': title,
               'actors': star,
               'rating': rating,
               'running_time': running_time,
               'uploaded' : uploaded
            }
        )
        sleep(.1)