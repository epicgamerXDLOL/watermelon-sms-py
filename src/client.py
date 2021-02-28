import socket
import threading
import watermelon
import tkinter

HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = ".disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)
window = tkinter.Tk()
window.title(socket.gethostbyname(socket.gethostname()))
tkinter.Label (window, text="Send a message",bg="black", fg="white") .grid(row=1, column=0)

textentry = tkinter.Entry(window, width=20, bg="white")
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

tkinter.Button(window, text="SUBMIT", width=6, command=tkinter_send) .grid(row=3, column=0, sticky="W")
window.mainloop()

