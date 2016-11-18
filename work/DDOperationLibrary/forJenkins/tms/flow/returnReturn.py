# -*- encoding:utf-8 -*-
import sys
# reload(sys)
# sys.setdefaultencoding('gbk')
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.express.expressFlow import ExpressFlow

__author__ = 'bida'

if __name__ == '__main__':
    if len(sys.argv) == 3:
        print '请输入运单号'.decode('utf-8')
        sys.exit(-1)

    ExpressFlow.express_return_return(account=sys.argv[1], order_ids=sys.argv[3].split(','),
                                      feedback_result=sys.argv[2])
