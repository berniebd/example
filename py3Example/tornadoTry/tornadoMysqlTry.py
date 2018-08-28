# -*- coding: utf-8 -*-
# Created by bida on 2018/8/17
from tornado.gen import coroutine
from tornado.ioloop import IOLoop
from tornado.web import RequestHandler, Application
from tornado_mysql import pools
pools.DEBUG = True
conn_param = {'host': '127.0.0.1', 'port': 3306, 'user': 'root', 'password': '1qaz@WSX', 'db': 'myself'}

class GetUserHandler(RequestHandler):
    POOL = pools.Pool(conn_param, max_idle_connections=1, max_recycle_sec=3, )

    @coroutine
    def get(self):
        user_id = self.get_argument('id')
        cursor = yield self.POOL.execute('select name from user where id = %s', user_id)
        if cursor.rowcount > 0:
            self.write({'status': 1, 'name': cursor.fetchone()[0]})
        else:
            self.write({'status': 0, 'name': ''})
        self.finish()

if __name__ == '__main__':
    application = Application([
        (r'/getuser', GetUserHandler)
    ], autoreload=True)
    application.listen(5001)
    IOLoop.current().start()