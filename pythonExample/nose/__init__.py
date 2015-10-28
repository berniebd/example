__author__ = 'bida'
def setup_module():
    f = open('c:/setupmodule.txt', 'a')
    f.write('setup module\n')

def teardown_module():
    f = open('c:/teardownmodule.txt', 'a')
    f.write('teardown module\n')