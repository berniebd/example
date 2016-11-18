# -*- encoding:utf-8 -*-
import unittest

import demjson
from common.httpRequest import HttpRequest
from keywords.portal.portalLogin import PortalLogin
from parameter.portal import envConfig
from parameter.portal.dealerEnum import Insurer
from util.portal.newCarUtil import NewCarUtil
from util.portal.vehicleUtil import VehicleUtil

__author__ = 'bida'


class NewCar:
    def __init__(self):
        pass

    @classmethod
    def quote(cls, dealer_name=u'', insurer_code=u'', vin=u'', brand_code=u'', model_name=u'',
              vehicle_tax_type=u'', abate_type=u'', abate_reason=u'', abate_proportion=u'',
              abate_amount=u''):
        """
        新车保单报价
        :param vin:
        :param dealer_name:经销商名称
        :param insurer_code: 保险公司编码
        :param brand_code: 品牌
        :param model_name: 车型名称
        :param vehicle_tax_type:纳税类型
        :param abate_type:减免方案
        :param abate_reason:减免原因
        :param abate_proportion:减免比例
        :param abate_amount:减免金额
        :return:
        """
        msg = u'新车保单报价'
        VehicleUtil.disconnect_vin_with_order(vin=vin)
        data = NewCarUtil.generate_quote_msg(dealer_name=dealer_name, insurer_code=insurer_code, vin=vin,
                                             brand_code=brand_code, model_name=model_name,
                                             vehicle_tax_type=vehicle_tax_type, abate_type=abate_type,
                                             abate_reason=abate_reason, abate_proportion=abate_proportion,
                                             abate_amount=abate_amount)
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg)
        obj = demjson.decode(response.text)
        if obj[u'status'] != u'100':
            raise StandardError(u'新车保单报价失败')
        return obj

    @classmethod
    def submit_policy(cls, order_no=u'', biz_special_clauses=[], ctp_special_clauses=[]):
        """
        新车保单投保
        :param ctp_special_clauses:
        :param biz_special_clauses:
        :param order_no:
        """
        msg = u'新车保单投保'
        data = {
            u"requestBodyJson":
                {
                    u"orderNo": order_no,
                    u"ctpSpecialClauses": ctp_special_clauses,
                    u"bizSpecialClauses": biz_special_clauses
                },
            u"transCode": u"TY1003"
        }
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg)
        return response
