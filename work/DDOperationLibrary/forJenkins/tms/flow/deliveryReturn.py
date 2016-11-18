# -*- encoding:utf-8 -*-
import sys
from time import sleep

# reload(sys)
# sys.setdefaultencoding('gbk')
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.base.baseInfo import BaseInfo
from keywords.tms.rainbow import RainbowFlow
from keywords.tms.express.expressFlow import ExpressFlow
from parameters.tms import tmsBase

__author__ = 'bida'

if __name__ == '__main__':
    print sys.getdefaultencoding()
    if len(sys.argv) == 7:
        print '请输入运单号'.decode('utf-8')
        sys.exit(-1)

    if BaseInfo.get_distributor_id(account='ADMIN', distributor_short_name=sys.argv[7].decode('gbk')) == 0:
        obj = BaseInfo.get_subdistributor_id(subdistributor_short_name=sys.argv[7].decode('gbk'))
        delivery_dealer = obj[0] + '-' + obj[1]
    else:
        delivery_dealer = BaseInfo.get_distributor_id(account='ADMIN', distributor_short_name=sys.argv[7].decode('gbk')) + '-'

    order_ids = sys.argv[6].split(',')

    RainbowFlow.sorting_forward_to_delivery_dealer(order_ids=order_ids,
                                                   delivery_dealer=delivery_dealer,
                                                   is_merchant=sys.argv[5] == 'False' and False or False,
                                                   account=sys.argv[2])
    sleep(tmsBase.wait_time)

    if sys.argv[4] == '1':
        # 配送失败退
        ExpressFlow.express_return_on_fail(order_ids=order_ids, express_account=sys.argv[3],
                                           operating_center_account=sys.argv[1])

    if sys.argv[4] == '2':
        # 换货成功退
        ExpressFlow.express_return_on_success(order_ids=order_ids, express_account=sys.argv[3])
