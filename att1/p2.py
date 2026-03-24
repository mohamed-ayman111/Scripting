from tkinter import *
import socket 
import threading 
from tkinter import messagebox
import webbrowser
import os
def statr_server():
    threading.Thread(target=Message_in,daemon=True).start()
def Message_in():
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:
            server_socket.bind(('localhost',12345))
            server_socket.listen(1)
            rackwan_socket, addr = server_socket.accept()
            with rakwan_socket:
                 while True:
                      message = rackwn_socket.recv(1024).decode('utf-8')
                      if message:
                           msg(mwssage)
def msg(message):
     if message == 'hi':
          messagebox.showinfo('Rakwan','Rakwan')