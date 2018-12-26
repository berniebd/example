# -*- coding: utf-8 -*-
# Created by bida on 2018/11/29

def func(a, b):
    """

    :param a:
    :param b:
    """
    print(a + b)

def run(f, args):
    f(*args)

if __name__ == '__main__':
    run(func, (1,2))