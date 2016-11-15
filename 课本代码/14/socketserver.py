#coding=utf-8
#server.py的升级版，引用了SocketServer，可以和client.py联合使用
from SocketServer import TCPServer,StreamRequestHandler
class Handler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print "Got connection from",addr
        self.wfile.write('thank you for conneting')

server = TCPServer(('',1234),Handler)
server.serve_forever()