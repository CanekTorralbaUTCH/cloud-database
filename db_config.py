"""Flask Configuration to connect to the database"""
from flask_pymongo import pymongo
import os

DB_USER = os.getenv("dbUser")
DB_PASSWORD = os.getenv("hydra111")
DB_NAME = os.getenv("DB_NAME")


client = pymongo.MongoClient("mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.9unw3.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = client.test
