#!usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8080

code = input('Insert code in python: ')

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    s.sendall(code.encode('utf-8'))
    print(s.recv(1024))
