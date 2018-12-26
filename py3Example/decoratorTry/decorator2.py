# -*- coding: utf-8 -*-
# Created by bida on 2018/10/8
import functools
import inspect


def de(f):
    @functools.wraps(f)
    def wrap_function(*args, **kwargs):
        kwargs['d'] = 'hello world'
        func_args = inspect.getcallargs(f, *args, **kwargs)
        return f(*args, **kwargs)

    return wrap_function


@de
def fu(a, **kwargs):
    print(a)
    # print(args[1])
    # print(args[2])
    # print(kwargs['c'])
    print(kwargs['d'])


if __name__ == '__main__':
    fu('a')
