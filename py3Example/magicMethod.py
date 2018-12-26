# -*- coding: utf-8 -*-
# Created by bida on 2018/9/17

class DistanceForm(object):
    def __init__(self, origin):
        self.origin = origin
        print(f'origin : {str(origin)}')

    def __call__(self, x):
        print(f'x : {x}')

if __name__ == '__main__':
    p = DistanceForm(1000)
    p(2000)