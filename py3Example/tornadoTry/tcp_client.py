# -*- coding: utf-8 -*-
# Created by bida on 2018/8/17

from tornado import ioloop, gen, iostream
from tornado.tcpclient import TCPClient

@gen.coroutine
def Trans():
    stream = yield TCPClient().connect('localhost', 8036)
    try:
        while True:
            DATA = input("Enter your input: ")
            yield stream.write(DATA.encode())
            back = yield stream.read_bytes(20, partial=True)
            print(back)
            if DATA == 'over':
                break
    except iostream.StreamClosedError:
        pass

if __name__ == '__main__':
    ioloop.IOLoop.current().run_sync(Trans)
