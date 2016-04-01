# -*- encoding:utf-8 -*-
import time
from datetime import datetime, timedelta

from keywords.portal.baseInfo import BaseInfo
from parameter.portal import template

__author__ = 'bida'


class NewCarUtil:
    def __init__(self):
        pass

    @classmethod
    def generate_vehicle_tax_msg(cls, vehicle_tax_type=u'', abate_type=u'', abate_reason=u'', abate_proportion=u'',
                                 abate_amount=u''):
        """
        生成新车投保车船税json
        :param vehicle_tax_type:
        :param abate_type:
        :param abate_reason:
        :param abate_proportion:
        :param abate_amount:
        :return:
        """
        vehicle_tax = template.vehicle_tax
        vehicle_tax[u'taxType'] = vehicle_tax_type
        vehicle_tax[u'payStartDate'] = datetime.today().strftime(u'%Y-%m-%d').decode()
        vehicle_tax[u'payEndDate'] = datetime.today().strftime(u'%Y-12-31').decode()
        vehicle_tax[u'taxAbateType'] = abate_type
        vehicle_tax[u'taxAbateReason'] = abate_reason
        vehicle_tax[u'taxAbateProportion'] = abate_proportion
        vehicle_tax[u'taxAbateAmount'] = abate_amount

        return vehicle_tax

    @classmethod
    def generate_vehicle_msg(cls, vin=u'', brand_code=u'', model_name=u''):
        """
        生成新车投保报价车辆信息json
        :param vin:
        :param brand_code:品牌
        :param model_name:大众车型名称
        :return:
        """
        if brand_code != u'':
            vehicle_info = BaseInfo.get_vehicle_info(vin=vin, brand_code=brand_code)[u'result']
            if len(vehicle_info) == 0:
                raise StandardError(u'根据vin，未找到符合条件的车辆')
            vehicle = vehicle_info[0]
            vehicle[u'purchasePrice'] = u''
            vehicle[u'currentValue'] = vehicle[u'purchasePriceTax']
            vehicle[u'licenseNo'] = u''
            vehicle[u'chgOwnerDate'] = u''
            vehicle[u'crossProvinceYear'] = u''
            vehicle[u'registerDate'] = datetime.today().strftime(u'%Y-%m-%d').decode()
            vehicle[u'usage'] = u'PERSON'
            vehicle[u'loanOrganization'] = u''
        if model_name != u'':
            model_info = BaseInfo.get_vw_module(model_name=model_name)[u'result']
            if len(model_info) == 0:
                raise StandardError(u'根据车型名称，未找到符合条件的车型')
            vehicle = model_info[0]
            vehicle[u'fuelType'] = u''
            vehicle[u'emptyWeight'] = vehicle[u'completemassMin']
            vehicle[u'carryingWeight'] = u''
            vehicle[u'vin'] = u'99887766554433221'
            vehicle[u'makeDate'] = u''
            vehicle[u'engineNo'] = u'998877665544321'
            vehicle[u'vehicleVariety'] = u'11'
            vehicle[u'insurercode'] = u''
            vehicle[u'packageId'] = u''
            vehicle[u'productId'] = u''
            vehicle[u'prodcutName'] = u''
            vehicle[u'packageName'] = u''
            vehicle[u'countryNature'] = u''
            vehicle[u'currentValue'] = u''
            vehicle[u'licenseNo'] = u''
            vehicle[u'chgOwnerDate'] = u''
            vehicle[u'crossProvinceYear'] = u''
            vehicle[u'registerDate'] = datetime.today().strftime('%Y-%m-%d').decode()
            vehicle[u'usage'] = u'PERSON'
            vehicle[u'loanOrganization'] = u''
            vehicle[u'exhaustScale'] *= 1000

        return vehicle

    @classmethod
    def generate_clause_msg(cls, dealer_name=u'', insurer_code=u''):
        """
        生成新车投保报价保险明细dict
        :param dealer_name:
        :param insurer_code:
        :return:
        """
        policy_clause = BaseInfo.get_policy_clause(dealer_name=dealer_name, insurer_code=insurer_code).json()[u'result']
        clause_info = []
        exist_new = False
        for value in policy_clause.itervalues():
            if value[u'code'] == u'NEW_EQUIPMENT':
                exist_new = True
            clause_info.append(value)
        return clause_info, exist_new

    @classmethod
    def generate_quote_msg(cls, dealer_name=u'', insurer_code=u'', vin=u'', brand_code=u'', model_name=u'',
                           vehicle_tax_type=u'', abate_type=u'', abate_reason=u'', abate_proportion=u'',
                           abate_amount=u''):
        """
        生成新车投保报价请求json
        :param dealer_name:
        :param insurer_code:
        :param vin:
        :param brand_code:
        :param model_name:
        :param vehicle_tax_type:
        :param abate_type:
        :param abate_reason:
        :param abate_proportion:
        :param abate_amount:
        :return:
        """
        content = template.quote_info
        insurer = BaseInfo.get_insure_info(dealer_name=dealer_name, insurer_code=insurer_code)
        content[u'requestBodyJson'][u'insurerCode'] = insurer[u'insurer']
        content[u'requestBodyJson'][u'agreementCode'] = insurer[u'agreementCode']
        content[u'requestBodyJson'][u'dealerCode'] = insurer[u'dealerCode']

        start_date = (datetime.today() + timedelta(days=1)).strftime('%Y-%m-%d 00:00')
        content[u'requestBodyJson'][u'ctpStartDate'] = start_date.decode()
        content[u'requestBodyJson'][u'bizStartDate'] = start_date.decode()

        party = template.party
        mobile = str(int(time.time())).decode() + u'0'
        party['owner']['mobile'] = mobile
        party['applicant']['mobile'] = mobile
        party['insured']['mobile'] = mobile
        content[u'requestBodyJson'][u'partyes'] = template.party

        content[u'requestBodyJson'][u'insuredVehicle'] = NewCarUtil.generate_vehicle_msg(brand_code=brand_code,
                                                                                         vin=vin,
                                                                                         model_name=model_name)
        clause_info, exist_new = NewCarUtil.generate_clause_msg(dealer_name=dealer_name, insurer_code=insurer_code)
        content[u'requestBodyJson'][u'coverages'] = clause_info
        if exist_new:
            content[u'requestBodyJson'][u'newEquipmentMOs'] = template.new_equipment

        content[u'requestBodyJson'][u'vehicleTax'] = NewCarUtil.generate_vehicle_tax_msg(vehicle_tax_type=vehicle_tax_type,
                                                                                         abate_type=abate_type,
                                                                                         abate_reason=abate_reason,
                                                                                         abate_proportion=abate_proportion,
                                                                                         abate_amount=abate_amount)

        return content
