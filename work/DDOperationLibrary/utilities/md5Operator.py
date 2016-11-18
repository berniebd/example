# -*- encoding:utf-8 -*-
import hashlib

__author__ = 'bida'


class MD5Operator:
    def __init__(self):
        pass

    @staticmethod
    def get_str_md5(src):
        m2 = hashlib.md5()
        m2.update(src)
        return m2.hexdigest()
