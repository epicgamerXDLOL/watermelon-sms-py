import socket
import threading
import watermelon
import tkinter
import json

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = ".disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

window = tkinter.Tk()
window.title("Watermelon SMS")
canvas = tkinter.Canvas(window, width=300, height=200)
greeting_message = ""

with open("../data/user_info.json", "r") as f:
    j = json.load(f)
    if str(socket.gethostname()) in j.keys():
        greeting_message = "Hello {}!".format(j[socket.gethostname()]["username"])
    else:
        tkinter.Label (window, text="Username: ",bg="black", fg="white") .grid(row=1, column=0)
        userbox = tkinter.Entry(window, width=100, bg="white")
        userbox.grid(row=2, column=0, sticky="W")
        passbox = tkinter.Entry(window, width=100, bg="white")
        passbox.grid(row=4, column=0, sticky="W")
        j[socket.gethostname()] = {"username": userbox.get(), "password": passbox.get()}
        with open("../data/user_info.json", "w") as w:
            json.dump(j, w, indent=4)
        greeting_message = "Hello {}!".format(userbox.get())

canvas.create_oval(50, 25, 250, 175, fill="white") 

tkinter.Label (window, text=greeting_message,bg="black", fg="white") .grid(row=1, column=0)

textentry = tkinter.Entry(window, width=100, bg="white")
textentry.grid(row=2, column=0, sticky="W")

def send(msg):
    message = msg.encode(FORMAT)
    msg_len = len(message)
    send_length = str(msg_len).encode(FORMAT)
    send_length += b" " * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)


def tkinter_send():
    send(textentry.get())

tkinter.Button(window, text="SUBMIT", width=100, command=tkinter_send) .grid(row=3, column=0, sticky="W")
window.mainloop()       

