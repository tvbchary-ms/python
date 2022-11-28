# This is a TCP/IP socket program in Python for Server

import socket

server_socket = socket.socket() # by default it is TCP, so not mentioning anything as args
print("socket created")

server_socket.bind(('localhost', 9898)) # port number rangers - 0-65535 exclude well-known ports below 1023

server_socket.listen(3)
print("waiting for connections")

while True:
    client_socket, client_addr = server_socket.accept()
    name = client_socket.recv(1024).decode()
    print("connected with", client_addr, name)

    client_socket.send(bytes(f"Welcome to TVBChary Server Mr/Ms {name}",'utf-8'))

    client_socket.close()