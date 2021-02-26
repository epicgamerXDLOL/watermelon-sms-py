import json
import random
def randomString(length:int, numberOfStrings= 1):

    string = [''.join([random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY1234567890') for i in range(length)])
             for i in range(numberOfStrings)]

    return string
class User:
    def __init__(self, username=None, password=None):
        self.username = username; self.password = password #initializing members
        with open("../data/user_info.json", "r") as f: #opening json file with the user data
            user_json = json.load(f)
        unique_id = False
        while not unique_id: 
            self.id = randomString(length=10)[0]
            if self.id not in user_json.keys(): #just in the very slim chance that the randomly generated string has already been genereated previously
                unique_id = True

    def signup(self):
        with open("../data/user_info.json", "r") as f:
            user_json = json.load(f)

        username = input("Username:\n")
        password = input("Password:\n")
        self.username, self.password = username, password
        user_json[self.id] = {"username":username, "password":password}
        with open("../data/user_info.json", "w") as f: #writing the username and password to the json file
            json.dump(user_json, f, indent=4)
