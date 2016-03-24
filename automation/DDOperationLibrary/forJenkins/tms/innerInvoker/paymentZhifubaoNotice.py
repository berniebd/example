# -*- encoding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.innerInvoker import InnerInvoker

__author__ = 'bida'

if __name__ == '__main__':
    for order_id in sys.argv[1].split(','):
        InnerInvoker.payment_zhifubao_notice(order_id=order_id, pay_status=sys.argv[2])