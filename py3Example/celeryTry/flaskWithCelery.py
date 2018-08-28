# -*- coding: utf-8 -*-
# Created by bida on 2018/8/13
from time import sleep

from arrow import Arrow
from celery import Celery
from flask import Flask


def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=app.config['CELERY_BROKER_URL'],
        backend=app.config['CELERY_RESULT_BACKEND'])
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery


flask = Flask(__name__)
flask.config.update(
    CELERY_BROKER_URL='redis://10.118.22.71:6379/7',
    CELERY_RESULT_BACKEND='redis://10.118.22.71:6379/8'
)

celery = make_celery(flask)


@celery.task(name='add_together')
def add_together(a, b):
    print(Arrow.now().format('YYYY-MM-DD HH:mm:ss'))
    return a + b


@flask.route('/', methods=['POST', 'GET'])
def tteest():
    r = add_together.apply_async(('a', 'b'), countdown=60)
    return Arrow.now().format('YYYY-MM-DD HH:mm:ss')


if __name__ == '__main__':
    flask.run(host='localhost', port=5001, debug=True)
