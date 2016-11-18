# -*- encoding:utf-8 -*-
from enum import Enum

__author__ = 'bida'


class Insurer(Enum):
    CPIC = u'太保'
    PICC = u'人保'
    GPIC = u'国寿财'


# 车船税类型
class VehicleTaxType(Enum):
    PAYING = u'纳税'
    REDUCTION = u'减税'
    COMPLETE = u'完税'
    FREE = u'免税'
    REJECT = u'拒缴'


# 减税类型
class AbateType(Enum):
    PERCENTAGE = u'按比例'
    AMOUNT = u'按金额'
    FREE = u'免税'


# 减税原因
class AbateReason(Enum):
    DEDUCTION_TAX = u'能源减免'
    REDUCTION_CERTI = u'具备减免税证明'
    DIPLOMATIC = u'外国使领馆'
    ARMY = u'军队武警'
    POLICE = u'警车'
    OTHER = u'其他'
