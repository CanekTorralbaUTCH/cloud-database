from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
import db_config as database

class Badges(Resource):
    """Get all badges"""
    def get(self):
        response = list(database.db.Badges.find())
        for doc in response:
            doc['_id'] = str(doc['_id'])

        return jsonify(response)
    
    def post(self):
        _ids = list(database.bd.Badges.insert_many([
            {
                'name':request.json[0]['name'],
                'last_name':request.json[0]['last_name'],
                'profile_picture':request.json[0]['profile_picture'],
                'hero_badge':request.json[0]['hero_badge'],
                'age':request.json[0]['age'],
                'city':request.json[0]['city'],
                'followers':request.json[0]['followers'],
                'likes':request.json[0]['likes'],
                'pictures':request.json[0]['pictures']
            },
            {
                'name':request.json[1]['name'],
                'last_name':request.json[1]['last_name'],
                'profile_picture':request.json[1]['profile_picture'],
                'hero_badge':request.json[1]['hero_badge'],
                'age':request.json[1]['age'],
                'city':request.json[1]['city'],
                'followers':request.json[1]['followers'],
                'likes':request.json[1]['likes'],
                'pictures':request.json[1]['pictures']
            },
        ]).inserted_ids)

        results = []

        for _id in _ids:
            result.append(str(_id))
        
        return jsonify({'inserted_ids':results})
    
    def delete(self):
        return database.db.Badges.delete_many({}).deleted_count