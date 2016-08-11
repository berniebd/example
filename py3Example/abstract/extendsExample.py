# -*- encoding:utf-8 -*-
__author__ = 'bida'

class A(object):
    def show(self):
        print('method show in class A!')


class B(object):
    def show(self):
        print('method show in class B!')

class C(B, A):

    def show(self):
        A.show(self)

if __name__ == '__main__':
    C().show()