# -*- encoding:utf-8 -*-
import hashlib
import requests
from parameters.tms import midExpressInvokerMessage
from utilities import DbOperator

__author__ = 'bida'


def get_md5(str):
    m = hashlib.md5()
    m.update(str)

    return m.hexdigest()


def prepare_middle_layer_route(warehouse_id, order_ids):
    sql = '''
      insert into order_route(order_id,warehouse_id,route_flag,creator,creation_date,modifier,last_modified_date)
      values ('%s', '%s', 1, 'MiddleLayerInvoker', '2015-12-28 15:28:27', 'MiddleLayerInvoker', '2015-12-28 15:28:27')
    '''
    for order_id in order_ids.split(','):
        DbOperator.execute_sql(db='middle_layer', sql=sql % (order_id, warehouse_id))


class MidExpressInvoker:
    def __init__(self):
        pass

    @classmethod
    def prepare_route(cls, order_ids='', warehouse_id='2'):
        prepare_middle_layer_route(warehouse_id, order_ids)

    @classmethod
    def middle_express_feedback_logistic_log(cls, express_id='', order_ids='', warehouse_id='2'):
        """
        快递公司中间层反馈物流信息
        :param express_id:
        :param order_ids:
        :param warehouse_id:
        """
        ids = order_ids.split(',')

        row = midExpressInvokerMessage.feedback_logistic_log_item.replace('${express_id}', express_id)
        rows = ''
        for order_id in ids:
            rows += row.replace('${order_id}', order_id)

        xml = midExpressInvokerMessage.xml.replace('${rows}', rows)
        print xml

        data = dict()
        data['para_xml'] = xml
        data['sign_type'] = 'MD5'
        data[
            'sign_str'] = order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness'
        data['sign_result'] = get_md5(
            order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness')

        requests.post(url='http://explinktest.ddexp.com.cn/api/order_log.php', data=data)

    @classmethod
    def middle_express_feedback(cls, express_id='', order_ids='', warehouse_id='2', order_status='101'):
        """
        快递中间层反馈配送信息
        :param order_status: 101,成功；102，在途；103 失败
        :param express_id:
        :param order_ids:
        :param warehouse_id:
        """
        reason_id = ''
        if order_status == '102':
            reason_id = '201'
        if order_status == '103':
            reason_id = '101'


        ids = order_ids.split(',')

        row = midExpressInvokerMessage.out_store_item.replace('${express_id}', express_id)\
            .replace('${order_status}', order_status)\
            .replace('${reason_id}', reason_id)
        rows = ''
        for order_id in ids:
            rows += row.replace('${order_id}', order_id)

        xml = midExpressInvokerMessage.xml.replace('${rows}', rows)
        print xml

        data = dict()
        data['para_xml'] = xml
        data['sign_type'] = 'MD5'
        data[
            'sign_str'] = order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness'
        data['sign_result'] = get_md5(
            order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness')

        requests.post(url='http://explinktest.ddexp.com.cn/api/feedback.php', data=data)

    @classmethod
    def middle_express_in_store(cls, express_id='', order_ids='', warehouse_id='2'):
        """
        快递中间层反馈入库
        :param express_id:
        :param order_ids:
        :param warehouse_id:
        """
        ids = order_ids.split(',')

        row = midExpressInvokerMessage.in_store_item.replace('${express_id}', express_id)
        rows = ''
        for order_id in ids:
            rows += row.replace('${order_id}', order_id)

        xml = midExpressInvokerMessage.xml.replace('${rows}', rows)
        print xml

        data = dict()
        data['para_xml'] = xml
        data['sign_type'] = 'MD5'
        data[
            'sign_str'] = order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness'
        data['sign_result'] = get_md5(
            order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness')

        requests.post(url='http://explinktest.ddexp.com.cn/api/in_store.php', data=data)

    @classmethod
    def middle_express_out_store(cls, express_id='', order_ids='', warehouse_id='2'):
        """
        快递中间层反馈出库
        :param express_id:
        :param order_ids:
        :param warehouse_id:
        """
        ids = order_ids.split(',')

        row = midExpressInvokerMessage.out_store_item.replace('${express_id}', express_id)
        rows = ''
        for order_id in ids:
            rows += row.replace('${order_id}', order_id)

        xml = midExpressInvokerMessage.xml.replace('${rows}', rows)
        print xml

        data = dict()
        data['para_xml'] = xml
        data['sign_type'] = 'MD5'
        data[
            'sign_str'] = order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness'
        data['sign_result'] = get_md5(
            order_ids + 'abcd1234567890abcdefgh1234567890abcdefgh1234567890abcdefgh' + '1100cchmjcollaboratormerriness')

        requests.post(url='http://explinktest.ddexp.com.cn/api/out_store.php', data=data)


if __name__ == '__main__':
    MidExpressInvoker.middle_express_in_store(express_id='1100', order_ids='151231112445147,151231112445148')
    MidExpressInvoker.middle_express_out_store(express_id='1100', order_ids='151231112445147,151231112445148')
    MidExpressInvoker.middle_express_feedback(express_id='1100', order_ids='151231112445147,151231112445148', order_status='101')
    MidExpressInvoker.middle_express_feedback_logistic_log(express_id='1100', order_ids='151231112445147,151231112445148')


