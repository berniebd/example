# -*- encoding:utf-8 -*-
import svn.remote

__author__ = 'bida'

if __name__ == '__main__':
    r = svn.remote.RemoteClient('http://svn.dangdang.com/repos')
    r.export('http://svn.dangdang.com/repos/test/bo.dangdang.com/CustomServicePlatform/3.30.7.25')