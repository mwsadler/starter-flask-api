from flask import Flask
import os
import boto3
dynamodb = boto3.resource('dynamodb')
db = dynamodb.Table('blue-long-gazelleCyclicDB')

app = Flask(__name__)

@app.route('/')
def hello_world():
    leo = db.put_item(
        Item={
            'pk': "partition_key",
            'sk': "sort_key",
            'type': "cat",
            'color': "orange"
        }
    )

    # get an item at key "partition_key", "sort_key" from the database
    item = db.get_item(Key={'pk': "partition_key", 'sk': "sort_key"})
    return item