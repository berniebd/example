# -*- encoding:utf-8 -*-
from common.dbExecutor import DbExecutor
from parameter.portal.dbConfig import DbAccount

__author__ = 'bida'


class VehicleUtil:
    def __init__(self):
        pass

    @classmethod
    def disconnect_vin_with_order(cls, vin=u''):
        sql = u"update PS_ORDER set vin = 'LSGAR5AL7FH240634' where vin = '%s'" % vin
        DbExecutor.update(DbAccount.POLICY, sql)

    @classmethod
    def get_available_vin(cls, brand_code=u''):
        """
        根据车牌号获取可用vin码
        :param brand_code:
        :return:
        """
        print u'*' * 20 + u'根据车牌号获取可用vin码'
        sql = u"select vin from vehicle_info where brand_code = '%s' and status = '01'" % brand_code
        result = DbExecutor.fetch_data(db=DbAccount.VEHICLE, sql=sql)
        if len(result) == 0:
            raise StandardError(u'无可用的vin码')
        print u'vin is' + result[0]
        return result[0]
