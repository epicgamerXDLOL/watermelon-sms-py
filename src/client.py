import socket
import threading
import watermelon
import tkinter
import random
import pymongo
from pymongo import MongoClient
import urllib

url = "mongodb+srv://water:AlwNL@cluster0.xrjyb.mongodb.net/Project0?retryWrites=true&w=majority"
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = ".disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cluster = MongoClient(url); db = cluster["user-info"]; collection = db[SERVER]
client.connect(ADDR)

if socket.gethostbyname(socket.gethostnme()) in cluster.find("")
post = {"username": f"User#{random.randint(1, 999999)}"}

collection.insert_one(post)


window = tkinter.Tk()
window.title("Watermelon SMS")
canvas = tkinter.Canvas(window, width=300, height=200)


tkinter.Label (window, text=f"Hello!",bg="black", fg="white") .grid(row=1, column=0)

textentry = tkinter.Entry(window, width=100, bg="white")
textentry.grid(row=0, column=0, sticky="W")

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def tkinter_send():
    send(textentry.get())

tkinter.Button(window, text="SEND", width=100, command=tkinter_send) .grid(row=3, column=0, sticky="W")
window.mainloop()       

