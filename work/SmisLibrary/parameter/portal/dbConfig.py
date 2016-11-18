# -*- encoding:utf-8 -*-
from enum import Enum

__author__ = 'bida'

ip = u'10.118.22.40'
service_name = u'sudbte'


class DbAccount(Enum):
    VEHICLE = {u'username': u'vehicledev', u'password': u'vehicledev'}
    POLICY = {u'username': u'policydev', u'password': u'policydev'}
    IISDEV = {u'username': u'iisdev', u'password': u'iisdev'}

