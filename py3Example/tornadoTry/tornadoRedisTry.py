# -*- coding: utf-8 -*-
# Created by bida on 2018/8/16
import tornado
from time import sleep

import tornadoredis
from tornado.gen import coroutine, Task
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application

pool = tornadoredis.ConnectionPool(host='10.118.22.71', max_connections=10, wait_for_available=True)
c = tornadoredis.Client(connection_pool=pool)
c.connect()

class MainHandler(RequestHandler):
    @coroutine
    def get(self):
        param1 = yield Task(c.get, 'param1')
        param2 = yield Task(c.get, 'param2')
        param3 = yield Task(c.get, 'param3')
        for item in [param1, param2, param3]:
            self.write(item if item else 'None')
            self.write('\n')
            self.flush()
            sleep(1)
        self.finish()

@tornado.gen.engine
def create_test_data():
    with c.pipeline() as pipe:
        pipe.set('param1', 'param1')
        pipe.set('param2', 'param2')
        pipe.set('param3', 'param3')
        yield tornado.gen.Task(pipe.execute)

if __name__ == '__main__':
    create_test_data()
    application = Application([
        ('/', MainHandler)
    ])
    application.listen(5001)
    IOLoop.current().start()
