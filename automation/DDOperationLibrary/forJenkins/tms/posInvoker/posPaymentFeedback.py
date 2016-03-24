# -*- encoding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.posInvoker import PosInvoker

if __name__ == '__main__':
    for order_id in sys.argv[1].split(','):
        PosInvoker.tms_pos_payment_feedback(order_no=order_id,
                                            pay_type=sys.argv[2],
                                            order_payable_amount=sys.argv[3])
