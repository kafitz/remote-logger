#!/usr/bin/env python3
# Kyle Fitzsimmons, 2019
from flask import Flask, Response, request
import logging
import os
from pymongo import MongoClient


client = MongoClient(os.environ.get('MONGO_HOST'),
                     port=27017,
                     username=os.environ.get('MONGO_USERNAME'),
                     password=os.environ.get('MONGO_PASSWORD'))
app = Flask(__name__)
logging.basicConfig(format='[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S %z')
logger = logging.getLogger('remote-logger')

database_name = os.environ.get('MONGO_DATABASE')
db_logs = client[database_name].logs

@app.route('/', methods=['GET'])
def index():
    return 'hello'

@app.route('/log', methods=['POST'])
def write_log():
    db_logs.insert_one(request.json)
    logger.info('Request logged.')
    return Response(status=201)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
