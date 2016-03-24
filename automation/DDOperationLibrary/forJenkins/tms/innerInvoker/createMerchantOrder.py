# -*- encoding:utf-8 -*-
import sys
import os

# reload(sys)
# sys.setdefaultencoding('gbk')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.innerInvoker import InnerInvoker

__author__ = 'bida'

if __name__ == '__main__':
    InnerInvoker.create_merchant_order(count=sys.argv[1],
                                       items=sys.argv[2],
                                       entrepot_id=sys.argv[3],
                                       receive_street_id=sys.argv[4],
                                       shipment_type=sys.argv[5],
                                       client_order_type=sys.argv[6],
                                       shop_id=sys.argv[7],
                                       distributor=sys.argv[9].decode('gbk'),
                                       pay_id=sys.argv[8],
                                       should_receive_payment=sys.argv[10],
                                       send_city=sys.argv[11])
