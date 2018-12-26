# -*- coding: utf-8 -*-
# Created by bida on 2018/8/14
from tornado import gen
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

class ExampleHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        delay = self.get_argument('delay', 5)
        yield gen.sleep(int(delay))
        times = yield self.delay_twice(int(delay))
        print(f'delay is {delay}, times is {times}')
        self.write({"status": 1, "times": times, "msg": "Success"})
        self.finish()

    @gen.coroutine
    def delay_twice(self, seconds):
        yield gen.sleep(seconds)
        yield gen.sleep(seconds)
        raise gen.Return(2)

class ExampleTwoHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        for _ in range(5):
            yield gen.sleep(3)
            self.write('zzzzzzzzzzzzz&lt;br&gt;')
            self.flush()
        self.finish()

class ExampleThreeHandler(RequestHandler):
    @gen.coroutine
    def post(self, *args, **kwargs):
        print(self)
        self.finish()

if __name__ == '__main__':
    application = Application([
        (r"/exampleOne", ExampleHandler),
        (r"/exampleTwo", ExampleTwoHandler),
        (r"/exampleThree", ExampleThreeHandler)
    ], autoreload=True)
    # method one
    application.listen(5003)
    # method two
    # Application autoreload must be False
    # server = HTTPServer(application)
    # server.bind(5003)
    # server.start(4)

    IOLoop.current().start()
