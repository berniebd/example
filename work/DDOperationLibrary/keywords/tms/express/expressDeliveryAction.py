# -*- encoding:utf-8 -*-
import demjson

from keywords.tms.tmsLogin import TmsLogin
import xlsxwriter
from parameters.tms import tmsBase
from parameters.tms.tmsBase import dispatchStatus
from utilities.httpRequest import HttpRequest

__author__ = 'bida'


def check_result(resp):
    print 'resp : [%s]' % resp
    if resp == '':
        print '!!!!!!!!!!result of uploading file is null'
    if resp != '' and demjson.decode(resp)['result'] == 'failed':
        raise StandardError('>>>>>>>>>>Operation Failed!')


class ExpressDeliveryAction:
    def __init__(self):
        pass

    @classmethod
    def batch_feedback(cls, account='AUTOEXPRESS', order_ids=[], feedback_result='SUCCESS'):
        """
        批量状态反馈
        :param account:
        :param order_ids:
        :param feedback_result: SUCCESS,FAIL,INTRANSIT
        """
        print u'*' * 20 + u'批量状态反馈'
        workbook = xlsxwriter.Workbook('batchFeedback.xlsx')
        worksheet = workbook.add_worksheet('Sheet 1')
        worksheet.write(0, 0, u'运单号')
        worksheet.write(0, 1, u'配送状态')
        worksheet.write(0, 2, u'原因')
        worksheet.write(0, 3, u'签收人')
        worksheet.write(0, 4, u'邮寄包裹号')
        line = 1
        for order_id in order_ids:
            print order_id
            worksheet.write(line, 0, order_id)
            worksheet.write(line, 1, dispatchStatus[feedback_result]['status'])
            worksheet.write(line, 2, dispatchStatus[feedback_result]['reason'])
            if feedback_result == 'SUCCESS':
                worksheet.write(line, 3, u'本人签收')
            worksheet.write(line, 4, order_id)
            line += 1
        workbook.close()

        url = tmsBase.base_url + '/tms/goods/expressGoodsStatusFeedBackController/upload.do'

        with open('batchFeedback.xlsx', 'rb') as f:
            files = {'uploadExcel': f}
            resp = HttpRequest.post_request(TmsLogin.get_session(account), url, files=files)
            check_result(resp)
            return resp

    @classmethod
    def batch_dispatch(cls, account='AUTOEXPRESS', order_ids=[]):
        """
        运单批量出库配送
        :param account:
        :param order_ids:
        """
        print u'*' * 20 + u'运单批量出库配送'
        workbook = xlsxwriter.Workbook('batchDispatch.xlsx')
        worksheet = workbook.add_worksheet('Sheet 1')
        worksheet.write(0, 0, u'运单号')
        worksheet.write(0, 1, u'配送员')
        worksheet.write(0, 2, u'配送员电话')
        line = 1
        for order_id in order_ids:
            print order_id
            worksheet.write(line, 0, order_id)
            worksheet.write(line, 1, u'张三')
            worksheet.write(line, 2, u'13800138000')
            line += 1
        workbook.close()

        url = tmsBase.base_url + '/tms/goods/expressGoodsArrivalOutStorageController/upload.do'
        with open('batchDispatch.xlsx', 'rb') as f:
            files = {'uploadExcel': f}
            resp = HttpRequest.post_request(TmsLogin.get_session(account), url, files=files)
            check_result(resp)
            return resp

    @classmethod
    def batch_in_storage(cls, account='AUTOEXPRESS', order_ids=[]):
        """
        运单到货批量入库
        :param account:
        :param order_ids:运单ids,list
        :return:
        """
        print u'*' * 20 + u'运单到货批量入库'
        workbook = xlsxwriter.Workbook('batchInStorage.xlsx')
        worksheet = workbook.add_worksheet('Sheet 1')
        worksheet.write(0, 0, u'运单号')
        line = 1
        for order_id in order_ids:
            print order_id
            worksheet.write(line, 0, order_id)
            line += 1
        workbook.close()

        url = tmsBase.base_url + '/tms/goods/expressGoodsArrivalToStorageController/upload.do'

        with open('batchInStorage.xlsx', 'rb') as f:
            files = {'uploadExcel': f}
            resp = HttpRequest.post_request(TmsLogin.get_session(account), url, files=files)
            check_result(resp)
            return resp
