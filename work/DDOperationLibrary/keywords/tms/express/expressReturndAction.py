# -*- encoding:utf-8 -*-
import re
from datetime import datetime
from time import sleep

import demjson

from keywords.tms.base.baseInfo import BaseInfo
from keywords.tms.express.expressUtil import ExpressUtil
from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


class ExpressReturnAction:
    def __init__(self):
        pass

    @classmethod
    def express_export_pre_return_order(cls, account='AUTOEXPRESS', order_ids=[]):
        """
        待上门退货单，导出PDF
        :param account:
        :param order_ids:
        """
        print u'*' * 20 + u'待上门退货单，导出PDF'
        obj = demjson.decode(ExpressUtil.express_get_return_order_info(account=account, order_ids=order_ids))
        ids = ''
        for item in obj['rows']:
            ids += item['id']
            ids += ','
        url = tmsBase.base_url + '/tms/goods/expressChangeReturnGoodsController/exportPDF.do?ids=' + ids
        resp = HttpRequest.get_request(TmsLogin.get_session(account), url)
        # print resp.decode('utf-8')

    @classmethod
    def express_confirm_distributor_return(cls, account='EXPRESS', order_ids=[]):
        """
        配送商退货
        :param account:
        :param order_ids:
        """
        print u'*' * 20 + u'配送商退货'
        obj = demjson.decode(ExpressUtil.express_get_distributor_return_info(account=account, order_ids=order_ids))
        n = 0
        while int(obj['total']) != len(order_ids) and n < tmsBase.retry_times:
            print 'expect %s, actual %s' % (len(order_ids), obj['total'])
            sleep(1)
            obj = demjson.decode(ExpressUtil.express_get_distributor_return_info(account=account, order_ids=order_ids))
            n += 1
        print 'expect %s, actual %s' % (len(order_ids), obj['total'])

        if int(obj['total']) != len(order_ids):
            print 'expect %s, actual %s' % (len(order_ids), obj['total'])
            raise StandardError(u'>>>>>>>>>>期望待退货运单,与实际可退货运单不一致')

        keys = ''
        for item in obj['rows']:
            keys += item['id']
            keys += ','

        url = tmsBase.base_url + '/tms/goods/expressReturnGoodsController/goReturnGoodsConfirmation.do?ids=' \
              + keys[:-1]

        resp = HttpRequest.get_request(TmsLogin.get_session(account), url)

        pattern_dis = re.compile(r'returnGoodsBatch" value="(.+)"/>')

        res_dis = pattern_dis.search(resp).groups()
        if len(res_dis) == 0:
            raise StandardError(u'未找到退货批次号')

        return_id = res_dis[0]
        print u'退货批次号 : ' + return_id

        print u'*' * 20 + u'确认退货'
        confirm_url = tmsBase.base_url + '/tms/goods/expressReturnGoodsController/confirm.do'
        confirm_resp = HttpRequest.post_request(TmsLogin.get_session(account), confirm_url,
                                                data={'ids': keys, 'returnGoodsBatch': return_id})
        print confirm_resp
        return return_id, confirm_resp

    @classmethod
    def express_confirm_direct_return(cls, account='AUTOEXPRESS', order_ids=[], distributor_short_name=''):
        """
        快递直退
        :param account:
        :param order_ids:
        :param distributor_short_name:
        :return:
        """
        print u'*' * 20 + u'快递直退'
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += '\n'

        obj = demjson.decode(ExpressUtil.express_get_direct_return_info(account=account, order_ids=order_ids))

        if int(obj['total']) != len(order_ids):
            raise StandardError(u'>>>>>>>>>>有错误的运单号')

        keys = ''
        for item in obj['rows']:
            keys += item['id']
            keys += ','

        url = tmsBase.base_url + '/tms/goods/expressReturnStraightGoodsController/returnStraight.do'

        data = dict()
        data['deliveryDealer'] = BaseInfo.get_distributor(short_name=distributor_short_name)
        data['ids'] = ids
        data['returnGoodsExpnumber'] = datetime.now().strftime('%y%m%d%H%M%S')

        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        print u'退货快递单号：' + data['returnGoodsExpnumber']
        print resp

        return data['returnGoodsExpnumber'], resp

# if __name__ == '__main__':
#     ExpressReturnAction.express_export_pre_return_order(order_ids=['151210162026267'])
