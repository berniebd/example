# -*- encoding:utf-8 -*-
import sys
from time import sleep
# reload(sys)
# sys.setdefaultencoding('gbk')
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.express.expressFlow import ExpressFlow

if __name__ == '__main__':
    ExpressFlow.express_delivery(account=sys.argv[1],
                                 target=sys.argv[3],
                                 order_ids=sys.argv[2].split(','),
                                 feedback_result=sys.argv[4])
