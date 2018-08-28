# -*- coding: utf-8 -*-
# Created by bida on 2018/8/10
from time import sleep

from celery import Celery
from celery.schedules import crontab

broker = 'redis://10.118.22.71:6379/5'
backend = 'redis://10.118.22.71:6379/6'
app = Celery('example2', broker=broker, backend=backend)

app.conf.timezone = 'UTC'
app.conf.beat_schedule = {
    'add-every-5-seconds': {
        'task': 'example.adds',
        'schedule': 5.0,
        'args': ('a', 'b')
    },
    'add-every-10-seconds': {
        'task': 'example.adds',
        'schedule': 10.0,
        'args': ('aa', 'bb')
    },
    'add-every-1-minute': {
        'task': 'example.adds',
        'schedule': crontab(),
        'args': ('aaa', 'bbb')
    }
}


# @app.on_after_configure.connect
# def setup_periodic_tasks(sender, **kwargs):
#     # every 10 seconds, 30 seconds
#     sender.add_periodic_task(30, adds.s('aa', 'bb'))
#     sender.add_periodic_task(10, adds.s('a', 'b'))
#     # every 1 minute
#     sender.add_periodic_task(crontab(), adds.s('aaa', 'bbb'))


@app.task(name='example.adds')
def adds(a, b):
    print(f'task add started {a}')
    sleep(2)
    print(f'task add started {b}')
    return a + b
#
#
# @app.task(name='example.subtracts')
# def subtracts(a, b):
#     print(f'task subtracts started {a}')
#     sleep(2)
#     print(f'task subtracts started {b}')
#     return a - b
#
#
# @app.task(name='example.divides')
# def divides(a, b):
#     print(f'task divides started {a}')
#     sleep(2)
#     print(f'task divides started {b}')
#     return a / b
