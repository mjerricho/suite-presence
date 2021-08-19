from flask import Flask, request, jsonify, Response, render_template
from flask_restful import Resource, Api
import pymongo

import json

import numpy as np
import ssl


try:
    mongo = pymongo.MongoClient("mongodb+srv://admin:f8lJiFSyeI7nRjRO@suitepresence.0orhr.mongodb.net/test",
        serverSelectionTimeoutMS = 1000)
    db = mongo.suite
    db = db.presence
    monngo.server_info()
except:
    print("Cannot connect to db")

app = Flask(__name__)
api = Api(app)

class loading(Resource):
    def get(self):

        #show page is loading while the html sends itself a post request to pull the data

        return render_template('loading.html')

    def post(self):
        mongo = pymongo.MongoClient("mongodb+srv://admin:f8lJiFSyeI7nRjRO@suitepresence.0orhr.mongodb.net/test",
            serverSelectionTimeoutMS = 1000)
        db = mongo.suite
        db = db.presence
