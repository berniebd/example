# -*- coding: utf-8 -*-
# Created by bida on 2018/8/1
import cx_Oracle

from DBUtils.PooledDB import PooledDB

pool = PooledDB(creator=cx_Oracle, user='monitor', password='monitor', dsn='10.118.22.40:1521/sudbte')
conn = pool.connection()
cursor = conn.cursor()
cursor.execute("select * from policyowner.ps_order where order_no = 'BK1800050949'")
print(cursor.fetchall())
