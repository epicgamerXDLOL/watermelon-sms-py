import socket
import threading
import tkinter
import pymongo
from pymongo import MongoClient
import urllib

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT_MESSAGE = ".disconnect"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)




def handle_client(conn, addr):
    print(f"New Connection: {addr}")
    
    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE: 
                connected = False
            url = "mongodb+srv://water:AlwNL@cluster0.xrjyb.mongodb.net/Project0?retryWrites=true&w=majority"
            cluster = MongoClient(url)
            db = cluster["user-info"]
            collection = db[addr[0]]
            username = collection.find({"username": ""})
            print('\n'.join(username))

    conn.close()
    print("\rEnded Session.")

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"active connections: {threading.activeCount() - 1}")

print("server starting...")
print(socket.gethostbyname(socket.gethostname()))
start()

