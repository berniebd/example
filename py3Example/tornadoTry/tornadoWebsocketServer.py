# -*- coding: utf-8 -*-
# Created by bida on 2018/8/16
from urllib.parse import urlparse
from tornado import ioloop
from tornado.web import Application
from tornado.websocket import WebSocketHandler

class EchoWebSocket(WebSocketHandler):
    CORS_ORIGINS = ['localhost']

    def check_origin(self, origin):
        parsed_origin = urlparse(origin)
        return parsed_origin.hostname in self.CORS_ORIGINS

    def open(self):
        print('WebSocket opened')

    def on_message(self, message):
        self.write_message(u'you said' + message)

    def on_close(self):
        print('WebSocket closed')

if __name__ == '__main__':
    application = Application([
        (r'/', EchoWebSocket)
    ])
    application.listen(5002)
    ioloop.IOLoop.current().start()