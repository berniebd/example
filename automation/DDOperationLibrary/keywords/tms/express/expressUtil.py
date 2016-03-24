# -*- encoding:utf-8 -*-
import demjson

from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


class ExpressUtil:
    def __init__(self):
        pass

    @classmethod
    def express_check_order_state(cls, account='AUTOEXPRESS', order_ids=[], state=''):
        """
        在快递系统验证运单状态
        :param account:
        :param order_ids:
        :param state:
        """
        obj = demjson.decode(cls.express_get_order_info(account=account, order_ids=order_ids))
        print u'*' * 20 + u'在快递系统验证运单状态'
        for item in obj['rows']:
            print '--------[%s] expected [%s], actual [%s]' % (item['waybillNumber'], state, item['waybillStatusName'])
            assert state == item['waybillStatusName']

    @classmethod
    def express_get_order_info(cls, account='AUTOEXPRESS', order_ids=[]):
        """
        查询运单信息
        :param account:
        :param order_ids:
        """
        print u'*' * 20 + u'在Express查询运单信息'
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += '\n'


        url = tmsBase.base_url + '/tms/waybill/expressWayBillController/datagrid.do?field=id,waybillNumber,deliverGoodsAddressName,deliverGoodsStorageName,waybillStatusName,deliverGoodsTime,putStorageTime,exprotStorageTime,distributionFeedbackTime,signTime,expectArrivalStarttime,expectArrivalEndtime,distributionUser,provinceName,cityName,districtName,streetName,detailAddress,goodsMoney,receiveMoney,caseNumbers,weight,volumeWeight,chargedWeight,customerMessage,waybillNumberSourceName,platformSourceName,distributionTypeName,customerBuyTime,differenceStatusName,packStandard,bestDeliverGoodsTime,payTypeName,interceptStatus,postPackNumber,expressNumber,payTypeName'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'waybillNumbers': ids})
        print resp
        return resp

    @classmethod
    def express_get_direct_return_info(cls, account='AUTOEXPRESS', order_ids=[]):
        """
        获取可快递直退的运单信息
        :param account:
        :param order_ids:
        """
        print u'*' * 20 + u'获取可快递直退的运单信息'
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += '\n'
        search_url = tmsBase.base_url + '/tms/goods/expressReturnStraightGoodsController/datagrid.do?field=id,waybillNumber,deliverGoodsStorage,deliverGoodsStorageName,returnGoodsAddress,deliveryDealer,deliveryDealerName,deliveryDealerSub,waybillNumberSource,waybillNumberSourceName,waybillType,waybillTypeName,waybillStatus,waybillStatusName,goodsMoney,shouldReturnMoney,deliverGoodsTime,distributionFeedbackTime,returnGoodsTime,returnGoodsExpnumber'
        search_resp = HttpRequest.post_request(TmsLogin.get_session(account), search_url, data={'waybillNumbers': ids})
        print search_resp
        return search_resp

    @classmethod
    def express_get_return_order_info(cls, account='AUTOEXPRESS', order_ids=[]):
        """
        获取待打印上门退货单信息
        :param account:
        :param order_ids:
        """
        print u'*' * 20 + u'获取待打印上门退货单信息'
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += '\n'
        search_url = tmsBase.base_url + '/tms/goods/expressChangeReturnGoodsController/datagrid.do?field=id,waybillNumber,previousWaybillNumber,waybillType,deliverGoodsTime,deliveryDealer,deliveryDealerSub,deliveryDealerSubName,deliverGoodsAddress,deliverGoodsStorage,addressee,addresseeMobile,countryId,countryName,provinceId,provinceName,cityId,cityName,districtId,districtName,streetId,streetName,detailAddress,returnGoods,returnGoodsCount,shouldReturnMoney,bestDeliverGoodsTime,operateUser,returnGoodsReason,customerMessage,returnGoodsPrice,returnGoodsTotalprice,remark,deliverGoodsAddressName,deliverGoodsStorageName'
        search_resp = HttpRequest.post_request(TmsLogin.get_session(account), search_url, data={'waybillNumbers': ids})
        print search_resp
        return search_resp

    @classmethod
    def express_get_distributor_return_info(cls, account='EXPRESS', order_ids=[]):
        """
        获取可配送商直退的运单信息
        :param account:
        :param order_ids:
        """
        print u'*' * 20 + u'获取可配送商直退的运单信息'
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += '\n'
        search_url = tmsBase.base_url + '/tms/goods/expressReturnGoodsController/datagrid.do?field=id,waybillNumber,deliverGoodsStorage,deliverGoodsStorageName,returnGoodsAddress,deliveryDealer,deliveryDealerName,deliveryDealerSub,waybillNumberSource,waybillNumberSourceName,waybillType,waybillTypeName,waybillStatus,waybillStatusName,goodsMoney,shouldReturnMoney,deliverGoodsTime,distributionFeedbackTime,returnGoodsTime'
        search_resp = HttpRequest.post_request(TmsLogin.get_session(account), search_url, data={'waybillNumbers': ids})
        print search_resp
        return search_resp
