# -*- encoding:utf-8 -*-
from common.httpRequest import HttpRequest
from keywords.portal.portalLogin import PortalLogin
from parameter.portal import envConfig

__author__ = 'bida'


class BaseInfo:
    def __init__(self):
        pass



    @classmethod
    def get_vw_module(cls, model_name=u''):
        """
        获取大众车型名称
        :param model_name:
        """
        msg = u'获取大众车型名称'
        data = {u'requestBodyJson': {u'modelName': model_name}, u'transCode': u'TY1024'}
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg).json()
        if response[u'status'] != u'100':
            raise StandardError(u'获取大众车型名称出错')
        return response

    @classmethod
    def get_vehicle_info(cls, vin=u'', brand_code=u''):
        """
        根据vin码获取车辆信息
        :param brand_code:
        :param vin:
        """
        msg = u'根据vin码获取车辆信息'
        request_body_json = {u'brandCode': brand_code, u'vin': vin}
        data = {u'requestBodyJson': request_body_json, u'transCode': u'PTA101'}
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg).json()
        if response[u'status'] != u'100':
            raise StandardError(u'获取车辆信息出错')
        return response

    @classmethod
    def get_account_info(cls):
        """
        获取当前登录用户信息
        """
        msg = u'获取当前登录用户信息'
        data = {u"requestBodyJson": {}, u"transCode": u"TY1016"}
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg)
        return response

    @classmethod
    def get_dealer_info_all(cls):
        """
        获取当前登录用户经销商信息
        """
        msg = u'获取当前登录用户的经销商信息'
        data = {u"requestBodyJson": {}, u"transCode": u"DTA101"}
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg)
        return response

    @classmethod
    def get_dealer_info(cls, dealer_name=''):
        """
        获取当前登录用户指定名称的经销商的信息
        :param dealer_name:
        """
        print u'*' * 20 + u'获取当前登录用户的名称为【' + dealer_name + u'】经销商信息'
        results = BaseInfo.get_dealer_info_all().json()[u'result']
        if len(results) == 0:
            raise StandardError(u'当前登录用户未配置经销商')
        dealer = None
        for result in results:
            if result[u'dealerName'] == dealer_name:
                dealer = result
                break
        if dealer is None:
            raise StandardError(u'未找到当前登录用户指定名称的经销商')
        return dealer

    @classmethod
    def get_insurer_info_all(cls, dealer_name=u''):
        """
        获取经销商保险公司信息
        :param dealer_name:
        :param dealer:
        """
        msg = u'获取经销商关联保险公司信息'
        dealer = BaseInfo.get_dealer_info(dealer_name=dealer_name)
        data = {u"requestBodyJson": dealer, u"transCode": u"DTA102"}
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg)
        return response

    @classmethod
    def get_insure_info(cls, dealer_name=u'', insurer_code=u''):
        """
        按名称获取经销商合作保险公司信息
        :param insurer_code:
        :param dealer_name:
        """
        print u'*' * 20 + u'获取选中经销商的合作保险公司【' + insurer_code + u'】'
        results = BaseInfo.get_insurer_info_all(dealer_name=dealer_name).json()[u'result']
        if len(results) == 0:
            raise StandardError(u'当前经销商无合作保险公司')
        insurer = None
        for result in results:
            if result['insurer'] == insurer_code:
                insurer = result
                break
        if insurer is None:
            raise StandardError(u'未找到经销商指定名称的合作保险公司')
        insurer[u'insurerCode'] = insurer[u'insurer']
        return insurer

    @classmethod
    def get_policy_clause(cls, dealer_name=u'', insurer_code=u''):
        """
        获取保险公司产品套餐
        :param dealer_name:
        :param insurer_code:
        """
        msg = u'获取保险公司产品套餐'
        data = {u"requestBodyJson": BaseInfo.get_insure_info(dealer_name=dealer_name, insurer_code=insurer_code),
                u"transCode": u"PTA102"}
        response = HttpRequest.post_data(PortalLogin.get_session(), envConfig.url, json_data=data, msg=msg)

        if response.json()[u'status'] != u'100':
            raise StandardError(u'获取保险产品套餐失败')
        return response