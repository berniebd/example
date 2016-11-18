# -*- encoding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.expressInvoker import ExpressInvoker

if __name__ == '__main__':
    ExpressInvoker.feedback_logistics_log(distributor_id=sys.argv[2],
                                          order_ids=sys.argv[1].split(','))
