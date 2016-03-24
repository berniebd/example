# -*- encoding:utf-8 -*-
import demjson
from keywords.tms.tmsLogin import TmsLogin
from parameters.tms import tmsBase
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


def check_operation_result(resp):
    print resp
    if demjson.decode(resp)['success'] == 'false':
        raise StandardError('>>>>>>>>>>Operation Failed!')


class DeliveryAction:
    def __init__(self):
        pass

    @classmethod
    def delivery_in_storage(cls, account='TIANJINSORTING', order_id=''):
        """
        运单入库
        :param account:
        :param order_id:
        :return:
        """
        print u'*' * 20 + u'运单入库'
        url = tmsBase.base_url + '/tms/sort/sortInStorageController/inStorage.do'

        resp = HttpRequest.post_request(TmsLogin.get_session(account),
                                        url,
                                        data={'orderNo': order_id})
        print resp
        return resp

    @classmethod
    def delivery_weight(cls, account='TIANJINSORTING', order_no='', weight_type=1, weight=10):
        """
        运单称重
        :param account:
        :param order_no:运单号，或运单号
        :param weight_type: 1：运单号，2：订单号
        :param weight:重量，默认10
        :return:
        """
        print u'*' * 20 + u'运单称重'
        url = tmsBase.base_url + '/tms/sort/sortGetWeightController/setWeight.do'
        data = dict()
        data['orderNo'] = order_no
        data['weight'] = weight
        data['weightType'] = weight_type

        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        check_operation_result(resp)
        return resp

    @classmethod
    def delivery_create_package(cls, account='TIANJINSORTING', package_no='', package_type=1):
        """
        创建合包
        :param account:
        :param package_no:合包号
        :param package_type: 合包类型，1:中转合包，2:配送合包，3:退货合包
        """
        print u'*' * 20 + u'创建合包'
        url = tmsBase.base_url + '/tms/sort/sortWaybillPackageController/checkpkgNo.do'
        data = dict()
        data['packageNo'] = package_no
        data['packageType'] = package_type

        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        check_operation_result(resp)
        return resp

    @classmethod
    def delivery_add_order_into_package(cls, account='TIANJINSORTING', order_no='', package_no='', package_type=1,
                                        weight=10):
        """
        合包添加运单
        :param account:
        :param order_no:运单号
        :param package_no: 合包号
        :param package_type: 合包类型，1:中转合包，2:配送合包，3:退货合包
        :param weight: 重量
        :return:
        """
        print u'*' * 20 + u'合包添加运单'
        url = tmsBase.base_url + '/tms/sort/sortWaybillPackageController/packageOrderTmp.do'

        data = {'orderNo': order_no, 'packageNo': package_no, 'packageType': package_type, 'weight': weight}
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        check_operation_result(resp)
        return resp

    @classmethod
    def delivery_delete_order_from_package(cls, account='TIANJINSORTING', order_no='', package_no=''):
        """
        从合包中删除运单
        :param account:
        :param order_no:
        :param package_no:
        :return:
        """
        print u'*' * 20 + u'从合包中删除运单'
        url = tmsBase.base_url + '/tms/sort/sortWaybillPackageController/delPackageOrderTmp.do?orderNo={order_no}&packageNo={package_no}' \
            .replace('{order_no}', order_no) \
            .replace('{package_no', package_no)
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url)
        check_operation_result(resp)
        return resp

    @classmethod
    def delivery_confirm_package(cls, account='TIANJINSORTING', package_no='', package_type=1, weight=10):
        """
        确认合包
        :param account:
        :param package_no: 合包号
        :param package_type: 合包类型，1:中转合包，2:配送合包，3:退货合包
        :param weight: 重量
        :return:
        """
        print '*' * 20 + u'确认合包'
        url = tmsBase.base_url + '/tms/sort/sortWaybillPackageController/packageOrder.do'
        data = {'packageNo': package_no, 'packageType': package_type, 'weight': weight}
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        check_operation_result(resp)
        return resp

    @classmethod
    def delivery_out_storage(cls, account='TIANJINSORTING', out_company='', order_no='', out_order_type=2, out_type=1,
                             outcountct=1, outcountdis=1):
        """
        运单出库
        :param account:
        :param out_company:出库公司
        :param order_no:单据号
        :param out_order_type:单据类型，1:运单号，2:合包号
        :param out_type:出库类型，1:出库到配送商,2：出库到城际运输商
        :param outcountct:
        :param outcountdis:
        :return:
        """
        print u'*' * 20 + u'运单出库'
        url = tmsBase.base_url + '/tms/sort/sortOutstorageController/outStorage.do'
        data = dict()
        data['outCmp'] = out_company
        data['orderNo'] = order_no
        data['outOrderType'] = out_order_type
        data['outType'] = out_type
        data['outcountct'] = outcountct
        data['outcountdis'] = outcountdis

        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data=data)
        check_operation_result(resp)
        return resp

    @classmethod
    def delivery_handoff(cls, account='TIANJINSORTING', out_type='1', out_company='', begin_date='', end_date=''):
        """
        出库交接
        :param account:
        :param out_type: 1:出库到配送商，3:出库到城际运输商
        :param out_company:
        :param begin_date:
        :param end_date:
        :return:
        """
        print u'*' * 20 + u'获取出库交接单'
        search_data = dict()
        search_data['handoverBeginDate'] = begin_date
        search_data['handoverEndDate'] = end_date
        search_data['outCmp'] = out_company
        search_data['outType'] = out_type
        search_data['page'] = '1'
        search_data['rows'] = '10'

        search_url = tmsBase.base_url + '/tms/sort/sortDeliveryHandoverController/handoverList.do?field=handoverId,outType,transfer,subtransfer,citytransfer,isCostly,startTime,endTime,traderName,countOrder,countPackage,rfCountOrder,rfCountPackage,diffOrder,diffPackage,operator'
        search_resp = HttpRequest.post_request(TmsLogin.get_session(account), search_url, data=search_data)
        print search_resp

        obj = demjson.decode(search_resp)

        if len(obj['rows']) == 0:
            raise StandardError(u'没有符合要求的交接单')

        handover_id = obj['rows'][0]['handoverId']
        print 'handoverId: ' + handover_id

        print u'*' * 20 + u'出库交接'
        url = tmsBase.base_url + '/tms/sort/sortDeliveryHandoverController/toHandover.do'
        resp = HttpRequest.post_request(TmsLogin.get_session(account), url, data={'ids': handover_id})
        check_operation_result(resp)

        return handover_id, resp

if __name__ == '__main__':
        search_data = dict()
        search_data['handoverBeginDate'] = ''
        search_data['handoverEndDate'] = ''
        search_data['outCmp'] = '99999998'
        search_data['outType'] = '1'
        search_data['page'] = '1'
        search_data['rows'] = '10'

        search_url = tmsBase.base_url + '/tms/sort/sortDeliveryHandoverController/handoverList.do?field=handoverId,outType,transfer,subtransfer,citytransfer,isCostly,startTime,endTime,traderName,countOrder,countPackage,rfCountOrder,rfCountPackage,diffOrder,diffPackage,operator'
        for i in range(100):
            search_resp = HttpRequest.post_request(TmsLogin.get_session('TIANJINSORTING'), search_url, data=search_data)
            print search_resp