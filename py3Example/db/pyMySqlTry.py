# -*- coding: utf-8 -*-
# Created by bida on 2018/8/17
import pymysql

connection = pymysql.connect(host='localhost', user='root', password='1qaz@WSX', db='myself')
try:
    with connection.cursor() as cursor:
        sql = "select * from user where id = %s"
        cursor.execute(sql, 1)
        result = cursor.fetchall()
        print(result)

finally:
    connection.close()

