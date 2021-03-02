import pymongo
import urllib
from pymongo import MongoClient
url = f"mongodb+srv://watermelonSmsUser:{urllib.parse.quote('2@U9NbWZKCicJE-')}@cluster0.xrjyb.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

cluster = MongoClient(url)
db = cluster["test"]
collection = db["test"]
post = {"_id": 2, "name": "bruh", "test": "mongo"}
collection.insert_one(post)
print("finished")