# -*- encoding:utf-8 -*-
__author__ = 'bida'


class Singleton():
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)

        return cls._instance
