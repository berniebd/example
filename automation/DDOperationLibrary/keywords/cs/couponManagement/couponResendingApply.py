# -*- encoding:utf-8 -*-
import sys
import os
from keywords.cs.baseAction.csLogon import CsLogon
from parameters.cs import csBase
from utilities.httpRequest import HttpRequest
__author__ = 'bida'


class CouponResendingApply:
    def __init__(self):
        pass

    @staticmethod
    def submit_resending_apply(coupon_id, customer_id, amount, order_id, reason):
        """
        提交礼券补发申请
        :param coupon_id:礼券申请编号
        :param customer_id: 用户id
        :param amount: 发放金额
        :param order_id: 订单号
        :param reason: 发放原因
        :return:
        """
        print u'*' * 20 + u'提交礼券补发申请'
        url = csBase.base_url + 'RandomCoupon/CouponApply'

        data = dict()
        data['CouponId'] = coupon_id
        data['CustId'] = customer_id
        data['Amount'] = amount
        data['OrderId'] = order_id
        data['Reason'] = reason

        resp = HttpRequest.post_request(CsLogon.get_session(), url, data=data)

        print resp

        return resp


# resp = CouponResendingApply.submit_resending_apply('43', '1', '10', '1', 'no reason')
