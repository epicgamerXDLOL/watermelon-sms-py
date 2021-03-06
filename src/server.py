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
user_fetched = ""

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    server.send(send_length)
    server.send(message)

def getUsernameFromDatabase(address):
    try:

        with open("../private/mongo_link.txt") as f:
            url = f.read()
        cluster = MongoClient(url)
        db = cluster["user-info"]
        collection = db[address]
        username = collection.find_one()["username"]
        return username

    except:
        print("Not a valid user.")


def handle_client(conn, addr):
    print(f"New Connection -> {getUsernameFromDatabase(addr[0])}")
    
    connected = True
    arbitrary_var = 0
    while connected:
        

        msg_len = conn.recv(HEADER).decode(FORMAT)
        if arbitrary_var == 0:
            user_fetched = getUsernameFromDatabase(addr[0])
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE: 
                connected = False
            print(f"{user_fetched}: {msg}")
        

        
        arbitrary_var += 1
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

