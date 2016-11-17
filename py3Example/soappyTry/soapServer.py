# -*- encoding:utf-8 -*-
__author__ = 'bida'

import SOAPpy

def hello():
    return 'hello world!'

server = SOAPpy.SOAPServer(('localhost', 8090))
server.registerFunction(hello)
server.server_forever()