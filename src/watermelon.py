import pymongo
import socket
import threading
import random
from pymongo import MongoClient

MONGO_LINK = "../private/mongo_link.txt"



class User:

    def __init__(self, ip_address:str, username=None, password=None, _id=None):

        self.username = username
        self.password = password
        self._id = _id
        self.ip_address = ip_address

    
    def sign_up(self, username, password):

        cred_post = {}
        with open(MONGO_LINK, "r") as f:
            url = f.read()

        obj_id = random.randint(1, 1000000000)

        cluster = MongoClient(url)
        db = cluster["users"]
        coll = db["user-credentials"]
        found_username = coll.find({"username": username})

        if not found_username:
            cred_post["_id"] = obj_id
            cred_post["username"] = username
            cred_post["password"] = password
            self.username = username; self.password = password; self._id = obj_id
            return True
        
        else:
            return False