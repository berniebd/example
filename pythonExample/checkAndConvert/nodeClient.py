# -*- encoding:utf-8 -*-
import requests

__author__ = 'bida'

resp = requests.post('127.0.0.1:1337',data='hello world')
print resp.text
