# -*- encoding:utf-8 -*-
import unittest2 as unittest2

__author__ = 'bida'

class Layer():
    @classmethod
    def setUp(cls):
        with open('c:\\nose2.txt') as f:
            f.write('setUp')

class TestClass(unittest2.TestCase):
    layer = Layer

    def test_method_3(self):
        assert False