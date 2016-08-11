# -*- encoding:utf-8 -*-
__author__ = 'bida'

def my_generator():
    yield 1
    yield 2
    yield 3


if __name__ == '__main__':
    g = my_generator()
    for i in g:
        print(i)