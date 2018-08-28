# -*- coding: utf-8 -*-
# Created by bida on 2018/8/14
from flask import Flask

from celeryTry.flaskWithCelery import add_together

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    add_together.delay('aaaa', 'bbbb')
    return 'success'


if __name__ == '__main__':
    app.run(host='localhost', port=5002, debug=True)