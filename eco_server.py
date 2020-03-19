#!usr/bin/env python3

import socket

HOST = '127.0.0.1'
PORT = 8080


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()

    conn, addr = s.accept()
    with conn:
        print('Connected',addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            else:
                exec(data)
                m=data
                conn.sendall(m)