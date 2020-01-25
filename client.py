import socket
import os, sys
import time

c = socket.socket()

addr = sys.argv[1]
port = int(sys.argv[2])
print(addr, port)


c.connect((addr, port))

count = 0
while True:
    count += 1
    data =  b'client'
    print('send:', data, count)
    c.sendall(data)
    echo = c.recv(1024)
    print('recv:', echo, count)
    time.sleep(1)