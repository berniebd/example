# -*- encoding:utf-8 -*-
import sys
import os
# reload(sys)
# sys.setdefaultencoding('gbk')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.innerInvoker import InnerInvoker

__author__ = 'bida'

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print '请输入订单号'.decode('utf-8')
        sys.exit(-1)
    else:
        InnerInvoker.wms_return_confirmation(order_ids=sys.argv[1], operation=sys.argv[2])