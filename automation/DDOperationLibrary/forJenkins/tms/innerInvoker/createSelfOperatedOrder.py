# -*- encoding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.innerInvoker import InnerInvoker

__author__ = 'bida'

if __name__ == '__main__':
    InnerInvoker.create_self_operated_order(count=sys.argv[1],
                                            entrepot_id=sys.argv[2],
                                            shipment_type=sys.argv[3],
                                            receive_street_id=sys.argv[4],
                                            distributor=sys.argv[5].decode('gbk'),
                                            armoney=sys.argv[6],
                                            order_type=sys.argv[7],
                                            pay_id=sys.argv[8],
                                            send_city=sys.argv[9])
