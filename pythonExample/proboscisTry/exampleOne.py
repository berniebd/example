# -*- encoding:utf-8 -*-
from proboscis import test, TestProgram
from proboscis.asserts import assert_equal, assert_true, assert_false

__author__ = 'bida'


@test()
class ProboscisClass:
    def __init__(self):
        pass

    @test(groups=['a'])
    def method_a(self):
        assert_equal('1', '2', '1=2?')

    @test(groups=['b'], depends_on_groups=['a'])
    def method_b(self):
        assert_true(True, 'True?')

    @test(groups=['c'], depends_on_groups=['b', 'a'], always_run=True)
    def method_c(self):
        assert_false(False, 'False?')


def run_tests():
    TestProgram().run_and_exit()


if __name__ == '__main__':
    run_tests()
