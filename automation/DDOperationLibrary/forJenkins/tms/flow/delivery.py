# -*- encoding:utf-8 -*-
import sys
import os
from time import sleep
import chardet

# reload(sys)
# sys.setdefaultencoding('gbk')


sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\..\\'))
from keywords.tms.base.baseInfo import BaseInfo
from keywords.tms.express.expressFlow import ExpressFlow
from keywords.tms.rainbow import RainbowFlow
from parameters.tms import tmsBase

if __name__ == '__main__':
    if len(sys.argv) != 9:
        print '请输入运单号'.decode('utf-8')
        sys.exit(-1)

    if BaseInfo.get_distributor_id(account='ADMIN', distributor_short_name=sys.argv[2].decode('gbk')) == 0:
        obj = BaseInfo.get_subdistributor_id(subdistributor_short_name=sys.argv[2].decode('gbk'))
        delivery_dealer = obj[0] + '-' + obj[1]
    else:
        delivery_dealer = BaseInfo.get_distributor_id(account='ADMIN',
                                                      distributor_short_name=sys.argv[2].decode('gbk')) + '-'
    order_ids = sys.argv[1].split(',')

    RainbowFlow.sorting_forward_to_delivery_dealer(order_ids=order_ids,
                                                   delivery_dealer=delivery_dealer,
                                                   is_merchant=sys.argv[3] == 'True' and True or False,
                                                   is_packaged=sys.argv[4] == 'True' and True or False,
                                                   account=sys.argv[7])
    target = sys.argv[5]
    if target != '0':
        sleep(tmsBase.wait_time)
        ExpressFlow.express_delivery(target=target,
                                     order_ids=order_ids,
                                     feedback_result=sys.argv[6],
                                     account=sys.argv[8])
