# -*- encoding:utf-8 -*-
import functools
import inspect

__author__ = 'bida'


def check(discount):
    def check_user(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            func_args = inspect.getcallargs(f, *args, **kwargs)
            # if kwargs.get('username') == 'admin':
            if func_args.get('username') == 'admin':
                raise Exception('admin is not allowed!')
            return f(*args, **kwargs) * discount
        return wrapper
    return check_user


class Clazz(object):
    @staticmethod
    @check(discount=2)
    def foo(username='', fruit=''):
        """
        Decorator Test Demo
        :param username:
        :param fruit:
        """
        print('hi {0},here is your {1}'.format(username, fruit))
        return 12

if __name__ == '__main__':

    # print(Clazz.foo.__doc__)
    # print(Clazz.foo.__name__)
    print(Clazz.foo(fruit='apple'))
    # Clazz.foo(username='admin', fruit='banana')