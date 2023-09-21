from flask import Flask
import os

from flask_cors import cross_origin

app = Flask(__name__)

@app.route('/')
@cross_origin()
def hello_world():
    return 'Hello, world markkkk!'