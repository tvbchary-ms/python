# This is a TCP/IP socket program in Python for Client
import socket
client_socket = socket.socket()

client_socket.connect(('127.0.0.1',9898))

name= input("Enter your name: ")
client_socket.send(bytes(name,'utf-8'))

print(client_socket.recv(1024).decode()) #buffer size is 1024 here