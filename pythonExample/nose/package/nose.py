__author__ = 'bida'


def test_method():
    print 'test method'
    assert True

def method():
    print 'method'
    assert True

class test_demo_class:
    def method_in_class(self):
        print 'method in class'
        assert True

    def test_method_in_class(self):
        print 'test method in class'
        assert True

class demo_class:
    def method_in_class(self):
        print 'method in class'
        assert True

    def test_method_in_class(self):
        print 'test method in class'
        assert True