# -*- encoding:utf-8 -*-
from time import sleep

from keywords.tms.billing.billingAction import BillingAction
from keywords.tms.billing.billingUtil import BillingUtil
from keywords.tms.rainbow import RefundAction
from parameters.tms import tmsBase
from utilities import DbOperator

__author__ = 'bida'


class BillingFlow:
    def __init__(self):
        pass

    @classmethod
    def billing_return_refund(cls, account='ADMIN', order_nos=[]):
        """
        生成退款账单
        :param account:
        :param order_nos:
        :return:
        """
        # 退款申请
        refund_apply_no = RefundAction.refund_apply(account=account, order_nos=order_nos)

        refund_apply_nos = list()
        refund_apply_nos.append(refund_apply_no)
        sleep(tmsBase.wait_time)
        # 退货确认
        BillingAction.billing_confirm_refund(account=account, refund_apply_nos=refund_apply_nos)
        sleep(tmsBase.wait_time)
        refund_bill_id = BillingUtil.billing_get_billId_by_apply_no(refund_apply_no)[0]
        print u'退款账单号：%s' % refund_bill_id

        refund_bill_ids = list()
        refund_bill_ids.append(refund_bill_id)
        BillingAction.billing_audit_refund(account=account, billing_order_ids=refund_bill_ids)

        BillingAction.billing_deduct_refund(account=account, billing_order_ids=refund_bill_ids)

        return refund_bill_id

#
# if __name__ == '__main__':
#     BillingFlow.billing_return_refund(order_nos=['151209163837632', '151209163837633'])
