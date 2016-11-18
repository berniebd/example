# -*- encoding:utf-8 -*-
from time import sleep

import demjson

from keywords.tms.rainbow import RainbowUtil
from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


def check_operation_result(resp):
    print resp
    if demjson.decode(resp)['success'] == 'false':
        StandardError('>>>>>>>>>>Operation Failed!')


class RefundAction:
    def __init__(self):
        pass

    @classmethod
    def return_check_requests(cls, account='TIANJINOPERATION', operate_type='1', order_ids=[]):
        """
        退货审核
        :param account:
        :param operate_type: 1:批准，2:二次配送
        :param ids:
        """
        print u'*' * 20 + u'退货审核'

        obj = obj = demjson.decode(RainbowUtil.rainbow_get_return_request(order_nos=order_ids))
        n = 0
        while int(obj['total']) != len(order_ids) and n < tmsBase.retry_times:
            print 'expect %s, actual %s' % (len(order_ids), obj['total'])
            sleep(1)
            obj = demjson.decode(RainbowUtil.rainbow_get_return_request(order_nos=order_ids))
            n += 1

        print 'expect %s, actual %s' % (len(order_ids), obj['total'])

        if int(obj['total']) != len(order_ids):
            print 'expect %s, actual %s' % (len(order_ids), obj['total'])
            raise StandardError(u'>>>>>>>>>>期望待退货审核运单,与实际可退货运单不一致')

        ids = list()
        for item in obj['rows']:
            ids.append(item['id'])

        url = tmsBase.base_url + '/tms/sort/refundOrderCheckController/updateCheckResult.do?operation=' + operate_type
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'ids[]': ids})
        check_operation_result(resp)
        return resp

    @classmethod
    def return_in_storage(cls, account='TIANJINSORTING', order_no=''):
        """
        退货入库
        :param account:
        :param order_no:
        :return:
        """
        print u'*' * 20 + u'退货入库'
        url = tmsBase.base_url + '/tms/sort/refundOrderController/inbound.do'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'orderNo': order_no})
        check_operation_result(resp)
        return resp

    @classmethod
    def return_out_storage(cls, account='TIANJINSORTING', order_no='', business_id='', to_sorting_center=''):
        """
        退货出库
        :param account:
        :param order_no:
        :param business_id:
        :param to_sorting_center:
        :return:
        """
        print u'*' * 20 + u'退货出库'
        url = tmsBase.base_url + '/tms/sort/refundOrderController/outbound.do'
        data = dict()
        data['orderNo'] = order_no
        data['businessId'] = business_id
        data['toSortingCenter'] = to_sorting_center
        if business_id == '':
            data['exFlag'] = '2'
        if to_sorting_center == '':
            data['exFlag'] = '1'

        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        check_operation_result(resp)
        return resp

    @classmethod
    def return_handover(cls):
        """
        退货交接
        """
        print u'*' * 20 + u'退货交接'

    @classmethod
    def return_confirm(cls, account='TIANJINSORTING', ids=[]):
        """
        退货签收确认
        :param account:
        :param ids:
        :return:
        """
        print u'*' * 20 + u'退货签收确认'
        url = tmsBase.base_url + '/tms/sort/refundOrderController/signConfirm.do'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=ids)
        check_operation_result(resp)
        return resp

    @classmethod
    def refund_apply(cls, account='ADMIN', order_nos=[]):
        """
        退款申请
        :param account:
        :param ids:
        """
        print u'*' * 20 + u'退款申请'
        # 获取运单id
        order_ids = []
        obj = demjson.decode(RainbowUtil.rainbow_get_refund_apply_info(account=account, order_ids=order_nos))
        for item in obj['rows']:
            order_ids.append(item['id'])
        # 申请退款
        url = tmsBase.base_url + '/tms/sort/refundOrderController/refundApply.do'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'ids[]': order_ids})
        # check_operation_result(resp)
        print resp

        # 获取退款申请号
        obj = demjson.decode(RainbowUtil.rainbow_get_refund_apply_info(account=account, order_ids=order_nos))

        refund_apply_no = obj['rows'][0]['refundApplyNo']
        print u'----------退款申请号：%s' % refund_apply_no

        return refund_apply_no


