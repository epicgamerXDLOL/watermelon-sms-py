import pymongo
import urllib
from pymongo import MongoClient
url = "mongodb+srv://water:AlwNL@cluster0.xrjyb.mongodb.net/Project0?retryWrites=true&w=majority"

client = pymongo.MongoClient(url)
db = client["test"]

collection = db["test"]
post = {"_id": 2, "name": "bruh", "test": "mongo"}
collection.insert_one(post)
print("finished")
