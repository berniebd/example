# -*- encoding:utf-8 -*-
from common.dbExecutor import DbExecutor
from keywords.portal.newCar import NewCar
from parameter.portal.dbConfig import DbAccount
from parameter.portal.dealerEnum import Insurer

__author__ = 'bida'

if __name__ == '__main__':
    # NewCar.quote(dealer_name=u'四川测试', insurer_code=Insurer.CPIC.name.lower().decode(),
    #              vin='LSGAR5AL7FH240631',
    #              brand_code=u'Cadillac')
    # NewCar.quote(dealer_name=u'山东SVW', insurer_code=Insurer.CPIC.name.lower().decode(), model_name=u'SVW71612LS')

    sql = 'select content from template_def where template_id = 71'
    result = DbExecutor.fetch_data(DbAccount.IISDEV, sql)
    print result
    print dir(result[0][0])
    print result[0][0].read()
    print type(result[0][0].read())