# -*- encoding:utf-8 -*-
from enum import Enum

__author__ = 'bida'

retry_times = 10
base_url = 'http://10.3.254.23:8080/dangwebx'

user = {
    'ADMIN': {'username': u'admin', 'password': u'123456'},
    'TIANJINSORTING': {'username': u'tianjinsorting', 'password': u'123456@qwert'},
    'TIANJINOPERATION': {'username': u'tianjincenter', 'password': u'123456@qwert'},
    'AUTOEXPRESS': {'username': u'autoexpress', 'password': u'123456@qwert'},
    'CESHI3': {'username': u'dg-kd-test3', 'password': u'1qaz2wsx#'},
    'GZZFTest003': {'username': u'ZFGZP', 'password': u'@root1234'},
    'SHZFTest002': {'username': u'zhangfan2', 'password': u'@root1234'},
    'TJZFTest001': {'username': u'zhangfan1', 'password': u'@root12345'}
}

database = {
    'tms': {
        'host': '10.3.254.27', 'user': 'rainbow', 'passwd': 'rainbow', 'charset': 'utf8'
    },
    'tms_tst_express': {
        'host': '10.3.254.27', 'dbname': 'tms_tst_express', 'user': 'tms_tst', 'passwd': 'password', 'port': '3306',
        'charset': 'utf8'
    },
    'tms_tst_billing': {
        'host': '10.3.254.27', 'dbname':'tms_tst_billing','user': 'rainbow', 'passwd': 'rainbow','port':3306, 'charset': 'utf8'
    },
    'middle_layer':{
        'host': '192.168.85.143', 'dbname': 'middle_layer_schema', 'user': 'writeuser', 'passwd': 'ddbackend', 'port': 3306, 'charset': 'utf-8'
    }
}

dispatchStatus = {
    'SUCCESS': {'status': u'配送成功', 'reason': u''},
    'FAIL': {'status': u'配送失败', 'reason': u'查无此人'},
    'INTRANSIT': {'status': u'配送在途', 'reason': u'家中无人'}
}

kafka_client = '10.3.254.26:9092'

md5_key = '123456'
wait_time = 10


class DispatchStatus(Enum):
    SUCCESS = {'status': u'配送成功', 'reason': u''},
    FAIL = {'status': u'配送失败', 'reason': u'查无此人'},
    INTRANSIT = {'status': u'配送在途', 'reason': u'家中无人'}


class KafkaTopics(Enum):
    RAINBOW = 'IT_ORD_TO_TMS'
    WMS = 'IT_TNT_TO_TMS'
    POS = 'IT_3PL_TNT_TO_TMS'
    EXPRESS = 'IT_3PL_TNT_TO_TMS'
