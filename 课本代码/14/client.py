#coding=utf-8
#一个小型客户机     与server连接
import socket
s = socket.socket()
host = '' #socket.gethostname()
port = 1234

s.connect((host,port))
print s.recv(1024)