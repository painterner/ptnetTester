import socket
import os, sys
import time

s = socket.socket()

addr = sys.argv[1]
port = int(sys.argv[2])
print(addr, port)

s.bind((addr, port))

s.listen(10)

conn, addr = s.accept()


count = 0
while True:
    count += 1
    data = conn.recv(1024)
    print('recv:', data, count)
    echo = b'server'
    print('send:', echo, count)
    conn.sendall(echo)
    time.sleep(1)