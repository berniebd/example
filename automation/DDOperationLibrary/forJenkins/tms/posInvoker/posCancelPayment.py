# -*- encoding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.posInvoker import PosInvoker

if __name__ == '__main__':
    for order_id in sys.argv[1].split(','):
        PosInvoker.tms_pos_cancel_payment(order_no=order_id)