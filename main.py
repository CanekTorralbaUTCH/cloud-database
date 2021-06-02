from flask import Flask, jsonify, request
from flask_restful import Api, Resource, reqparse, abort
from flask_pymongo import pymongo
from bson.json_util import dumps, ObjectId
import db_config as database

app=Flask(__name__)
api=Api(app)

class Test(Resource):
    def get(self):
        return jsonify({"message":"Test ok, you are connected"})

class Badge(Resource):
    def get(self, by, data):
        response = self.abort_if_not_exist(by, data)
        response['_id'] = str(response['_id'])
        return jsonify(response)

    def post(self):
        _id = str(database.db.Badges.insert_one(
            {
                'name':request.json['name'],
                'last_name':request.json['last_name'],
                'profile_picture':request.json['profile_picture'],
                'hero_badge':request.json['hero_badge'],
                'age':request.json['age'],
                'city':request.json['city'],
                'followers':request.json['followers'],
                'likes':request.json['likes'],
                'pictures':request.json['pictures']
            }
        ).inserted_id)

        return jsonify({"_id":_id})

    def abort_if_not_exist(self, by, data):
        if by =="_id":
            response = database.db.Badges.find_one({"_id":ObjectId(data)})
        else:
            response = database.db.Badges.find_one({f"{by}":data})
        
        if response:
            return response
        else:
            abort(jsonify({"status":404, f"{by}":f"{data} not found"}))


class AllBadge(Resource):
    """Get all badges"""
    def get(self):
        pass 

api.add_resource(Badge,'/new/','/<string:by>:<string:data>/')
api.add_resource(AllBadge,'/all/','/delete/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True)