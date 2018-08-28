# -*- coding: utf-8 -*-
# Created by bida on 2018/8/10
from datetime import timedelta
from time import sleep
#
from celery import Celery
from celery.schedules import crontab
from celery.task import periodic_task


broker = 'redis://10.118.22.71:6379/15'
backend = 'redis://10.118.22.71:6379/14'
app = Celery('celeryTry', broker=broker, backend=backend)

app.conf.update(
    timezone='Asia/Shanghai',
    enable_utc=True,
    beat_schedule={
        "taks_1": {
            "task": 'celeryTryk.notice',
            'schedule': timedelta(seconds=15),
            'args': (12345, 56789)
        }
    }
)

@periodic_task(run_every=crontab(), name='celeryTry.notice')
def notice(start, end):
    print(f'shchduled task started!---{start}')
    sleep(5)
    print(f'scheduled task ended!---{end}')
    return True


