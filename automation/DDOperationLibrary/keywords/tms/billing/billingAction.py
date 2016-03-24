# -*- encoding:utf-8 -*-
import demjson

from keywords.tms.billing.billingUtil import BillingUtil
from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


class BillingAction():
    def __init__(self):
        pass

    @classmethod
    def billing_confirm_refund(cls, account='ADMIN', refund_batch_nos=[], refund_apply_nos=[]):
        """
        退货确认
        :param account:
        :param refund_batch_nos:退货批次号
        :param refund_apply_nos: 退款申请号
        """
        print u'*' * 20 + u'退货确认'
        url = tmsBase.base_url + '/tms/bms/billingRefundConfirmController/sure.do'
        rows = demjson.decode(
            BillingUtil.billing_get_pre_return_confirmed(account=account, refund_batch_nos=refund_batch_nos,
                                                         refund_apply_nos=refund_apply_nos))['rows']

        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'rows': demjson.encode(rows)})

        print resp

    @classmethod
    def billing_audit_refund(cls, account='ADMIN', billing_order_ids=''):
        """
        退款账单审核
        :param account:
        :param billing_order_ids:
        """
        print u'*' * 20 + u'退款账单审核'
        url = tmsBase.base_url + '/tms/bms/billingRefundBillController/audit.do'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'ids': billing_order_ids})
        print resp

    @classmethod
    def billing_deduct_refund(cls, account='ADMIN', billing_order_ids=''):
        """
        退款账单可低收款
        :param account:
        :param billing_order_ids:
        """
        print u'*' * 20 + u'退款账单可低收款'
        url = tmsBase.base_url + '/tms/bms/billingRefundBillController/changeDeductStatus.do'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'ids': billing_order_ids})
        print resp
