#coding=utf-8
#一个小型服务器        与client连接
import socket
s = socket.socket()
host = '' #socket.gethostname()
port = 1234
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    print 'Got connection from', addr
    c.send('thank you for connectting')
    c.close()