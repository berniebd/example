# -*- encoding:utf-8 -*-
import sys
from time import sleep
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.interface.posInvoker import PosInvoker
from keywords.tms.interface.innerInvoker import InnerInvoker
from keywords.tms.base.baseInfo import BaseInfo
from keywords.tms.rainbow import RainbowFlow, RainbowUtil
from keywords.tms.express.expressFlow import ExpressFlow
from keywords.tms.express.expressUtil import ExpressUtil
from parameters.tms import tmsBase

__author__ = 'bida'

if __name__ == '__main__':
    order_ids = InnerInvoker.create_self_operated_order(count=2)[0]

    sleep(tmsBase.wait_time)

    if BaseInfo.get_distributor_id(account='ADMIN', distributor_short_name='autoexpress') == 0:
        obj = BaseInfo.get_subdistributor_id(subdistributor_short_name='autoexpress')
        delivery_dealer = obj[0] + '-' + obj[1]
    else:
        delivery_dealer = BaseInfo.get_distributor_id(account='ADMIN', distributor_short_name='autoexpress') + '-'

    RainbowFlow.sorting_forward_to_delivery_dealer(order_ids=order_ids,
                                                   delivery_dealer=delivery_dealer,
                                                   account='TIANJINSORTING')
    sleep(tmsBase.wait_time)
    ExpressFlow.express_delivery(target='2',
                                 order_ids=order_ids,
                                 feedback_result='SUCCESS',
                                 account='AUTOEXPRESS')

    sleep(tmsBase.wait_time)
    for order_id in order_ids:
        # pos撤销支付
        PosInvoker.tms_pos_cancel_payment(order_no=order_id)

    sleep(tmsBase.wait_time)
    ExpressUtil.express_check_order_state(order_ids=order_ids, state='配送失败'.decode('utf-8'))
    RainbowUtil.rainbow_check_order_state(order_ids=order_ids, state='配送失败'.decode('utf-8'))
