# -*- coding: utf-8 -*-
# Created by bida on 2018/8/2
from time import sleep

import tornado
from tornado.ioloop import IOLoop

from tornado.web import RequestHandler, Application


class MainHandler(RequestHandler):
    def get(self):
        self.write('Hello world!')


class SecondaryHandler(RequestHandler):
    def post(self):
        self.write('secondary application')

    def on_finish(self):
        sleep(10)
        print('operation on SecondaryHandler finished')


def make_app():
    return Application([
        (r'/', MainHandler),
        (r'/secondary', SecondaryHandler)
    ], debug=True)


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    IOLoop.current().start()
