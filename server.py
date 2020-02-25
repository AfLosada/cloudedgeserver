from flask import Flask
from flask import request
import logging
from flask_redis import FlaskRedis
import os
import sys
import redis

app = Flask(__name__)
redis_client = FlaskRedis(app)

conn = redis.Redis("localhost", port=6379)

@app.route('/')
def hello_world():
    key = conn.randomkey()
    val = int(conn.get(key))

    return factorial(val)

def factorial(val):
    temp = 1
    for i in range(1,val):
        temp = temp * i
    return temp
app.run()