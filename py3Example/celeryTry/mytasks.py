# -*- coding: utf-8 -*-
# Created by bida on 2018/8/6

from celery import Celery
from celery import Task
from celery import task
broker = 'redis://10.118.22.71:6379/5'
backend = 'redis://10.118.22.71:6379/6'
app = Celery(broker=broker, backend=backend)


class MyTask(Task):
    def on_success(self, retval, task_id, args, kwargs):
        print('{0!r} successed {1!r}'.format(task_id, retval))

@app.task(base=MyTask, name='example.adds')
# @app.task(base=MyTask)
def adds(x, y):
    print(f'invoked by remote: adds {x}, {y}')
    return x + y


@app.task(base=MyTask, name='two.subtracts')
def subtract(x, y):
    print(f'invoked by remote: subtracts {x}, {y}')
    return x - y

