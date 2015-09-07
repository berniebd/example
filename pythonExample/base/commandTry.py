import sys

__author__ = 'bida'

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print 'please input soma params'
    else:
        print len(sys.argv)
        for arg in sys.argv:
            print arg