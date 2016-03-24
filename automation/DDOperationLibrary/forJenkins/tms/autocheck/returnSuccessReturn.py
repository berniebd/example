# -*- encoding:utf-8 -*-
import sys
from time import sleep
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.innerInvoker import InnerInvoker
from keywords.tms.express.expressFlow import ExpressFlow
from keywords.tms.express.expressUtil import ExpressUtil
from keywords.tms.rainbow import RainbowUtil
from parameters.tms import tmsBase

__author__ = 'bida'

if __name__ == '__main__':
    order_ids = InnerInvoker.create_change_and_refund_order(count=2, operate_type='3')[0]
    sleep(tmsBase.wait_time)

    ExpressFlow.express_return_return(account='AUTOEXPRESS', order_ids=order_ids)

    sleep(tmsBase.wait_time)
    ExpressUtil.express_check_order_state(order_ids=order_ids, state='退货已签收'.decode('utf-8'))
    RainbowUtil.rainbow_check_order_state(order_ids=order_ids, state='退货已签收'.decode('utf-8'))
