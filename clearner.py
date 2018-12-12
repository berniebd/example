# -*- coding: utf-8 -*-
# Created by bida on 2018/12/12
import os
import platform
import signal
import socket
import subprocess

from flask import Flask

app = Flask(__name__)

@app.route('/clean', methods=['POST', 'GET'])
def clean():
    if platform.system() == 'Windows':
        os.system('taskkill /im chrome.exe')
        os.system('taskkill /im chromedriver.exe')
    else:
        proc = subprocess.Popen(['pgrep', 'Chrome', 'chromedriver'], stdout=subprocess.PIPE)
        for pid in proc.stdout:
            os.kill(int(pid), signal.SIGTERM)
    return 'success'


if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 80))
    host = s.getsockname()[0]
    app.run(host=host, port=10001)

