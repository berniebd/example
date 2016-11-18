# -*- encoding:utf-8 -*-
import os

import cx_Oracle

from parameter.portal import dbConfig
from parameter.portal.dbConfig import DbAccount

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

__author__ = 'bida'


class DbExecutor:
    def __init__(self):
        pass

    @classmethod
    def fetch_data(cls, db=DbAccount.VEHICLE, sql=u''):
        with cx_Oracle.connect(db.value[u'username'], db.value[u'password'],
                               dbConfig.ip + u':1521/' + dbConfig.service_name) as conn:
            cur = conn.cursor()
            print u'sql is:' + sql
            cur.execute(sql)
            result = cur.fetchall()
            return result

    @classmethod
    def update(cls, db=DbAccount.VEHICLE, sql=u''):
        with cx_Oracle.connect(db.value[u'username'], db.value[u'password'],
                               dbConfig.ip + u':1521/' + dbConfig.service_name) as conn:
            cur = conn.cursor()
            print u'sql is:' + sql
            cur.execute(sql)

# if __name__ == '__main__':
#     with cx_Oracle.connect('vehicledev', 'vehicledev', '10.118.22.40:1521/sudbte') as connection:
#         print connection
#
#         cursor = connection.cursor()
#         cursor.execute('select model_name from insurer_model  where model_code = \'KDAAMD0002\'')
#         results = cursor.fetchall()
#         print results[0][0]
