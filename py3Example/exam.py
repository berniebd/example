# -*- encoding:utf-8 -*-
import json
import re
from datetime import datetime, date
from inspect import isfunction

import demjson

__auth__ = 'bida'

def call(a, b):
    return a + b

class Cla(object):
    def fun(self):
        pass

    @classmethod
    def class_fun(cls):
        pass

    @staticmethod
    def static_fun2():
        pass

if __name__ == '__main__':
    from inspect import isfunction
    add = lambda a, b: a+ b
    if hasattr(add, '__call__'):
        print(add(1, 2))
    if callable(add):
        print(add(2, 3))
    if isfunction(add):
        print(add(1, 5))
    if hasattr(call, '__call__'):
        print(call(1, 2))
    if callable(call):
        print(call(2, 3))
    if isfunction(call):
        print(call(1, 5))

    print(type(call))
    cla = Cla()
    print(type(Cla.class_fun))
    print(type(cla.class_fun))
    print(type(Cla.static_fun2))
    print(type(cla.static_fun2))
    print(type(Cla.fun))
    print(type(cla.fun))
