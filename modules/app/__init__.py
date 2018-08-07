import os
import json
import datetime
from flask import Flask
from bson.objectid import ObjectId
from flask_pymongo import PyMongo

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return json.JSONEncoder.default(self,o)

app = Flask(__name__)

app.config['MONGO'] = os.environ.get('DB')
mongo = PyMongo(app=app)

app.json_encoder = JSONEncoder

from app import *