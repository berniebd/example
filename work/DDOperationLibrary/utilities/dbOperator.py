
import MySQLdb
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..\\..\\'))
from parameters.tms import tmsBase
__author__ = 'bida'

database = {
    'tms': {
        'host': '10.3.254.27', 'user': 'rainbow', 'passwd': 'rainbow', 'charset': 'utf8'
    },
    'tms_tst_express': {
        'host': '10.3.254.27', 'dbname':'tms_tst_express','user': 'tms_tst', 'passwd': 'password','port':3306, 'charset': 'utf8'
    },
    'tms_tst_billing': {
        'host': '10.3.254.27', 'dbname':'tms_tst_billing','user': 'rainbow', 'passwd': 'rainbow','port':3306, 'charset': 'utf8'
    }
}

class DbOperator:
    def __init__(self):
        pass

    _connections = dict()

    @classmethod
    def get_database_connection(cls, db):
        if db not in cls._connections.keys():
            connection = MySQLdb.connect(host=tmsBase.database[db]['host'],
                                         user=tmsBase.database[db]['user'],
                                         db=tmsBase.database[db]['dbname'],
                                         passwd=tmsBase.database[db]['passwd'])
            cls._connections[db] = connection

        return cls._connections[db]

    @classmethod
    def fetch_data(cls, db, sql):
        connection = MySQLdb.connect(host=tmsBase.database[db]['host'],
                                     user=tmsBase.database[db]['user'],
                                     db=tmsBase.database[db]['dbname'],
                                     passwd=tmsBase.database[db]['passwd'],
                                     charset=tmsBase.database[db]['charset'])
        cur = connection.cursor()

        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        connection.close()
        print result
        return result

    @classmethod
    def execute_sql_many(cls, db, sql, params):
        conn = cls.get_database_connection(db)
        cur = conn.cursor()

        result = cur.executemany(sql, params)
        cur.close()

        return result

    @classmethod
    def execute_sql(cls, db, sql):
        conn = cls.get_database_connection(db)
        cur = conn.cursor()

        result = cur.execute(sql)
        cur.close()

        return result

    @classmethod
    def dd_execute_sql_string(cls,db, sql):
        # conn = cls.get_database_connection(db)
        thost=database[db]['host']
        tuser=database[db]['user']
        tpasswd=database[db]['passwd']
        tdb=database[db]['dbname']
        tport=database[db]['port']
        tcharset=database[db]['charset']
        try:
          connection = MySQLdb.connect(host=thost,
                                     user=tuser,
                                     passwd=tpasswd,
                                     db=tdb,
                                     port=tport,
                                     charset=tcharset)
          cur = connection.cursor()
          result = cur.execute(sql)
          connection.commit()
          tt = cur.fetchone()

        except MySQLdb.Error,e:
          print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        finally:
          cur.close()
          connection.close()
          return result, tt

