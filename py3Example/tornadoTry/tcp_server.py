# -*- coding: utf-8 -*-
# Created by bida on 2018/8/17

from tornado import ioloop, gen, iostream
from tornado.ioloop import IOLoop
from tornado.tcpserver import TCPServer


class MyTcpServer(TCPServer):
    @gen.coroutine
    def handle_stream(self, stream, address):
        try:
            while True:
                msg = yield stream.read_bytes(20, partial=True)
                print(msg.decode())
                yield stream.write(msg[::-1])
                if msg == b'over':
                    stream.close()
        except iostream.StreamClosedError:
            pass


if __name__ == '__main__':
    server = MyTcpServer()
    server.listen(8036)
    server.start()
    IOLoop.current().start()
