from nose import with_setup

__author__ = 'bernie'

def setUp():
    print 'setup'

def tearDown():
    print 'teardown'

def start():
    print 'user setup'


def end():
    print 'user teardown'


# @with_setup(start, end)
def test_method():
    print 'test method'
    assert False