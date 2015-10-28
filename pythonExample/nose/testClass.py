from nose.tools.nontrivial import with_setup

__author__ = 'bida'

# def setup_module():
#     f = open('c:/setupmodule.txt', 'a')
#     f.write('setup module\n')
#
# def teardown_module():
#     f = open('c:/teardownmodule.txt', 'a')
#     f.write('teardown module\n')

def setup():
    f = open('c:/setup.txt', 'a')
    f.write('setup method\n')

def teardown():
    f = open('c:/teardown.txt', 'a')
    f.write('teardown method\n')

def start():
    f = open('c:/setup.txt', 'a')
    f.write('customer setup method\n')

def end():
    f = open('c:/teardown.txt', 'a')
    f.write('customer teardown method\n')

@with_setup(start, end)
def test_method_4():
    print 'test method 4'
    assert False

def test_method_5():
    print 'test method 5'
    assert False

class TestClass:
    @classmethod
    def setup_class(cls):
        f = open('c:/setupclass.txt', 'a')
        f.write('setup class\n')

    @classmethod
    def teardown_class(cls):
        f = open('c:/teardownclass.txt', 'a')
        f.write('teardown class\n')

    def setup(self):
        f = open('c:/setup.txt', 'a')
        f.write('setup method in class\n')

    def teardown(self):
        f = open('c:/teardown.txt', 'a')
        f.write('teardown method in class\n')

    def test_method(self):
        print 'test method 1'
        assert False

    def test_method_2(self):
        print 'test method 2'
        assert False

class TestClass2:
    def test_method_3(self):
        print 'test method 3'
        assert False

