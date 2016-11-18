# -*- encoding:utf-8 -*-
import re

import demjson

from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


class RainbowUtil:
    def __init__(self):
        pass

    @classmethod
    def rainbow_check_order_state(cls, account='ADMIN', order_ids=[], state=''):
        """
        在Rainbow系统验证运单状态
        :param account:
        :param order_ids:
        :param state:
        """
        obj = demjson.decode(cls.rainbow_get_order_info(account=account, order_ids=order_ids))
        print u'*' * 20 + u'在Rainbow系统验证运单状态'
        for item in obj['rows']:
            print '--------[%s] expected [%s], actual [%s]' % (item['orderId'], state, item['currentStatusName'])
            assert state == item['currentStatusName']

    @classmethod
    def rainbow_get_refund_apply_info(cls, account='ADMIN', order_ids=[]):
        """
        查询退款申请
        :param account:
        :param order_ids:
        :return:
        """
        print u'*' * 20 + u'查询退款申请'
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += '\n'
        url = tmsBase.base_url + '/tms/sort/refundOrderController/dgRefundApply.do?field=id,orderNo,refundBatchNo,refundApplyNo,refundStatus,sortingCenter,refundWarehouse,orderType,orderSourceType,status,disTrader,subDisTrader,businessId,quantity,weight,amount,dueAmount,realAmount,expressNo,refundTime,shipTime,refundTime_begin,refundTime_end,refundInboundTime,refundInboundTime_begin,refundInboundTime_end,refundInboundTip,refundInboundBy,refundOutboundTime,refundOutboundTime_begin,refundOutboundTime_end,refundOutboundBy,refundDeliveryNo,refundDeliveryBy,refundSignTime,refundSignTime_begin,refundSignTime_end,toSortingCenter,'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'orderNos': ids})

        return resp


    @classmethod
    def rainbow_get_order_info(cls, account='ADMIN', order_ids=[]):
        """
        查询运单信息
        :param account:
        :param order_id:
        :return:
        """
        print u'*' * 20 + u'在Rainbow查询运单信息'
        ids = ''
        for order_id in order_ids:
            ids += order_id
            ids += '\n'
        url = tmsBase.base_url + '/tms/sort/sortIntegratedQueryController/datagrid.do?field=id,orderId,extOrderId,expressId,sortCenterIdName,warehouseIdName,currentStatusName,creationDate,putStorageTime,deliveryDate,transferPutStorageTime,transferDeliveryDate,distributionFeedbackTime,signTime,expectedDtStart,expectedDtEnd,toProvinceIdName,toCityIdName,toDivisionIdName,toStateIdName,toAddress,amount,dueAmount,quantity,weight,volume,chargedWeight,customerMessage,orderSourceName,orderSourcePlatformName,distributionModeName,shopName,orderDate,differenceStatusName,packSpec,bestArriveDate,payType,payTypeName,interceptStatus,mailPackId'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'waybillNumbers': ids})
        print resp
        return resp

    @classmethod
    def rainbow_get_order_count_in_storage(cls, account='TIANJINSORTING'):
        """
        查询当前用户当前已入库运单数

        :return: :raise Exception:
        """
        print u'*' * 20 + u'查询当前用户当前已入库运单数'
        url = tmsBase.base_url + '/tms/sort/sortInStorageController/instorageList.do?clickFunctionId=4028e0bb4d4be7c0014d4bec91220006'
        resp = HttpRequest.post_request(TmsLogin().get_session(account), url)
        # print resp
        pattern = re.compile(r'incount">(\d+)</font>')
        res = pattern.search(resp).groups()
        if len(res) == 0:
            raise StandardError('未找到已入库运单数')
        else:
            print res[0]
            return res[0]

    @classmethod
    def rainbow_list_order_in_storage(cls, account='TIANJINSORTING'):
        """
        显示当前用户已入库运单信息

        :return:
        """
        print u'*' * 20 + u'显示当前用户已入库运单信息'
        url = tmsBase.base_url + '/tms/sort/sortInStorageController/showInStoragePage.do?field=id,orderNo,deliveryWarehouse,disTrader,storageType,storageTime,storageTips,storageOperator'
        resp = HttpRequest.post_request(TmsLogin().get_session(account), url)
        print resp
        return resp

    @classmethod
    def rainbow_get_order_count_weighted(cls, account='TIANJINSORTING'):
        """
        查询当前用户当前已称重运单数

        :return: :raise Exception:
        """
        print u'*' * 20 + u'查询当前用户当前已称重运单数'
        url = tmsBase.base_url + 'tms/sort/sortGetWeightController/getWeightList.do?clickFunctionId=4028e0bb4d4be7c0014d4bec5e530004'
        resp = HttpRequest.post_request(TmsLogin().get_session(account), url)
        # print resp
        pattern = re.compile(r'weightcount">(\d+)</font>')
        res = pattern.search(resp).groups()
        if len(res) == 0:
            raise StandardError('未找到已称重运单数')
        else:
            return res[0]

    @classmethod
    def rainbow_list_order_weighted(cls, account='TIANJINSORTING'):
        """
        显示当前用户已称重运单信息

        :return:
        """
        print u'*' * 20 + u'显示当前用户已称重运单信息'
        url = tmsBase.base_url + '/tms/sort/sortGetWeightController/showGetWeightPage.do?field=id,orderNo,disTrader,subDisTrader,weight,weightTime,weightBy'
        resp = HttpRequest.post_request(TmsLogin().get_session(account), url)
        print resp
        return resp

    @classmethod
    def rainbow_list_package_detail(cls, account='TIANJINSORTING', package_no='', package_type=1):
        """
        查询合包明细
        :param package_no:
        :param package_type:1:中转合包，2:配送合包，3:退货合包
        """
        print u'*' * 20 + u'查询合包明细'
        url = tmsBase.base_url + '/tms/sort/sortWaybillPackageController/showPackagePage.do?packageNo={package_no}&packageType={package_type}&field=id,packageNo,orderNo,packageType,packageScanTime,packageBy,isPackage' \
            .replace('package_no', package_no) \
            .replace('package_type', package_type)

        resp = HttpRequest.post_request(TmsLogin().get_session(account), url)
        print resp
        return resp

    @classmethod
    def rainbow_get_order_count_out_storage(cls, account='TIANJINSORTING'):
        """
        查询当前用户已出库运单数

        :return: : 配送商出库数，城际运输商出库数
        """
        print u'*' * 20 + u'查询当前用户已出库运单数'
        url = tmsBase.base_url + '/tms/sort/sortOutstorageController/outstorageList.do?clickFunctionId=4028e0bb4d4be7c0014d4bf020b4000c'
        resp = HttpRequest.post_request(TmsLogin().get_session(account), url)
        # print resp

        pattern_dis = re.compile(r'outcountdis">(\d+)</font>')
        pattern_ct = re.compile(r'outcountct">(\d+)</font')

        res_dis = pattern_dis.search(resp).groups()
        if len(res_dis) == 0:
            raise StandardError(u'未找到出库到配送商的运单数')

        res_ct = pattern_ct.search(resp).groups()
        if len(res_ct) == 0:
            raise StandardError(u'未找到出库到城际运输商的运单数')

        return res_dis[0], res_ct[0]

    @classmethod
    def rainbow_get_return_request(cls, account='TIANJINOPERATION', order_nos=''):
        """
        查询退货申请
        :param account:
        :param order_nos:
        :return:
        """
        print u'*' * 20 + u'查询退货申请'
        url = tmsBase.base_url + '/tms/sort/refundOrderCheckController/datagrid.do?field=id,orderNo,deliveryWarehouse,refundAddress,disTrader,orderSourceType,orderType,feedbackTime,feedbackTime_begin,feedbackTime_end,failReason,amount,amount_begin,amount_end,dueAmount,dueAmount_begin,dueAmount_end,paidAmount,paidAmount_begin,paidAmount_end,refundType,shippedTime,shippedTime_begin,shippedTime_end,checkedResult,checkedTime,checkedTime_begin,checkedTime_end,checkedBy,'
        data = dict()
        ids = ''
        for order_no in order_nos:
            ids += order_no
            ids += '\n'
        data['orderNos'] = ids

        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        # print resp
        return resp