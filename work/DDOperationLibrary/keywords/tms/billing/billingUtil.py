# -*- encoding:utf-8 -*-
import MySQLdb
import demjson

from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities import DbOperator
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


class BillingUtil:
    def __init__(self):
        pass

    @classmethod
    def billing_check_refund_order_state(cls, account='ADMIN', refund_bill_id='', status='', deduct_status=''):
        """
        验证退款账单状态
        :param account:
        :param refund_bill_id:
        :param status:
        :param deduct_status:
        """

        refund_bill_ids = list()
        refund_bill_ids.append(refund_bill_id)
        obj = demjson.decode(
            BillingUtil.billing_get_refund_order_info(account=account, refund_order_ids=refund_bill_ids))
        print u'*' * 20 + u'验证退款账单状态，和退款可抵状态'
        print '[%s], expected status [%s],actual [%s]' % (refund_bill_id, status, obj['rows'][0]['status'])
        assert status == obj['rows'][0]['status']
        print '[%s], expected deduct status [%s],actual [%s]' % (refund_bill_id, deduct_status, obj['rows'][0]['deductStatus'])
        assert deduct_status == obj['rows'][0]['deductStatus']

    @classmethod
    def billing_get_billId_by_apply_no(cls, apply_no):
        """
        按退款申请在db查询退款账单
        :param apply_no:
        :return:
        """
        print u'*' * 20 + u'按退款申请在db查询退款账单'
        sql = "select refund_bill_id from billing_refund_bill_detail where refund_apply_no = '%s'" % apply_no
        result = DbOperator.fetch_data('tms_tst_billing', sql)
        if len(result) == 0:
            raise StandardError(u'退款申请[%s]无对应退款账单' % apply_no)
        else:
            refund_bill_id = result[0]

        return refund_bill_id

    @classmethod
    def billing_get_pre_return_confirmed(cls, account='ADMIN', refund_batch_nos=[], refund_apply_nos=[]):
        """
        退货确认页面查询
        :param account:
        :param refund_apply_nos:
        """
        print u'*' * 20 + u'退货确认页面查询'
        refund_batch_ids = ''
        for refund_batch_id in refund_batch_nos:
            refund_batch_ids += refund_batch_id
            refund_batch_ids += '\n'
        refund_apply_ids = ''
        for refund_apply_id in refund_apply_nos:
            refund_apply_ids += refund_apply_id
            refund_apply_ids += '\n'
        url = tmsBase.base_url + '/tms/bms/billingRefundConfirmController/datagrid.do?field=distributionTrade,distributionTradeName,orderId,refundBatchNo,refundApplyNo,refundAmount,orderType,orderStatus'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url,
                                        data={'refundApplyNo': refund_apply_ids, 'refundBatchNo': refund_batch_ids})

        return resp

    @classmethod
    def billing_get_refund_order_info(cls, account='ADMIN', refund_order_ids=[]):
        """
        账单退款审核页面查询
        :param account:
        :param refund_order_ids:
        """
        print u'*' * 20 + u'账单退款审核页面查询'
        billIds = ''
        for refund_order_id in refund_order_ids:
            billIds += refund_order_id
            billIds += '\n'
        url = tmsBase.base_url + '/tms/bms/billingRefundBillController/datagrid.do?field=id,distributionTrade,refundAmount,commonAmount,exchangeAmount,billDate,checkUser,checkDatetime,auditingUser,auditingDatetime,status,deductStatus,deductDatetime'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'billIds': billIds})

        return resp
#
#
# if __name__ == '__main__':
#     result = BillingUtil.billing_get_billId_by_apply_no('TKSQ1512170015')
#     print result
