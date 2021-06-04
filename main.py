from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_pymongo import pymongo
import db_config as database

#Resources
from res.badge import Badge
from res.badges import Badges

app=Flask(__name__)
api=Api(app)

@app.route('/all/adults/')
def get_adults():
    response = list(database.db.Badges.find({'age': 5}))

    for document in response:
        document["_id"] = str(document['_id'])
    
    return jsonify(response)


api.add_resource(Badge,'/new/','/<string:by>:<string:data>/')
api.add_resource(Badges,'/all/','/delete/all/')

if __name__ == '__main__':
    app.run(load_dotenv=True)