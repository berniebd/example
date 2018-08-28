# -*- coding: utf-8 -*-
# Created by bida on 2018/8/16
from time import time
from arrow import Arrow
from tornado.gen import coroutine
from tornado.ioloop import PeriodicCallback, IOLoop


@coroutine
def count():
    print(Arrow.now().format('YYYY-MM-DD HH:mm:ss.SSS'))

@coroutine
def ring():
    print(Arrow.now().format('YYYY-MM-DD HH:mm:ss.SSS'))

if __name__ == '__main__':
    PeriodicCallback(count, 1000).start()
    IOLoop.current().start()

    loop = IOLoop.current()
    print(Arrow.now().format('YYYY-MM-DD HH:mm:ss.SSS'))
    loop.call_at(time() + 10, ring)
    loop.call_later(10, ring)
    loop.start()