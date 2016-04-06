__author__ = 'bernie'

class TestClass:
    @staticmethod
    def setup_class():
        print 'setup in module'

    @staticmethod
    def setup():
        print 'setup in class'

    @staticmethod
    def teardown():
        print 'teardown in class'

    def testMethod_1(self):
        print 'test method 1 in class'
        assert False

    # def testMethod_2(self):
    #     print 'test method 2 in class'
    #     assert False