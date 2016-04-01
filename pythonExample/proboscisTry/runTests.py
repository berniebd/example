# -*- encoding:utf-8 -*-
from proboscis import register

__author__ = 'bida'

def run_tests():
    from exampleOne import ProboscisClass
    from exampleTwo import ProboscisClassTwo

    register(groups=['3a'], depends_on_groups=['a'])
    register(groups=['3b'], depends_on_groups=['b'])
    register(groups=['3c'], depends_on_groups=['c'])

if __name__ == '__main__':
    run_tests()