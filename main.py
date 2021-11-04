from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify, redirect
from bson.objectid import ObjectId
import json
import pymongo
from flask_pymongo import PyMongo
from flask.helpers import url_for
from bson import json_util
from flask_cors import CORS, cross_origin


app = Flask(__name__)

cors = CORS(app)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/favInfo'
app.config['CORS_Headers'] = 'Content-Type'
mongo = PyMongo(app)


@app.route('/', methods=['GET'])
def retrieveAll():
    data = list()
    collection = mongo.db.favInfo
    for i in collection.find():
       data.append({'name': i['name'], 'gender': i['gender'], 'age': int(i['age'])})
    return jsonify(data)


@app.route('/<name>', methods=['GET'])
@cross_origin()
def retrieveFromName(name):
    collection = mongo.db.favInfo
    data = collection.find_one({"name": name})
    return jsonify({"name": data['name'], "gender": data['gender']})


@app.route('/postData', methods=['POST'])
def postData():
    collection = mongo.db.favInfo
    name = request.json['name']
    gender = request.json['gender']
    age = int(request.json['age'])
    collection.insert_one({'name': name, 'gender': gender, 'age': age})
    return jsonify({'name': name, 'gender': gender, 'age': age})


@app.route('/deleteData/<name>', methods=['DELETE'])
def deleteData(name):
    collection = mongo.db.favInfo
    collection.delete_one({'name': name})
    return {}


@app.route('/update/<name>', methods=['PUT'])
def updateData(name):
    collection = mongo.db.favInfo
    updatedName = request.json['name']
    gender = request.json['gender']
    age = request.json['age']
    collection.update_one({'name': name}, {"$set": {'name': updatedName}})
    return jsonify({'name': updatedName, 'gender': gender, 'age': age})


if __name__ == '__main__':
    app.run(debug=True)

