import socket
import threading
import watermelon
import tkinter
import random
import pymongo
from pymongo import MongoClient
import urllib


HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = ".disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

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

