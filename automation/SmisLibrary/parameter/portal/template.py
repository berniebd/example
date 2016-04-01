# -*- encoding:utf-8 -*-
__author__ = 'bida'
quote_info = {
    u"requestBodyJson": {
        u"inputMode": u"1",
        u"insuredMode": u"STANDARD",
        u"insurerCode": u"",
        u"agreementCode": u"",
        u"marketingId": u"",
        u"dealerCode": u"",
        u"orderNo": u"",
        u"bizStartDate": u"",
        u"ctpStartDate": u"",
        u"isSelectedCTP": u"1",
        u"bizActualDiscount": u"",
        u"insuredVehicle": None,
        u"partyes": None,
        u"coverages": None,
        u"premiumFloating": {},
        u"businessType": u"AUTO_NEW",
        u"rcdUnpolicyRequestMO": None,
        u"vehicleTax": {},
        u"platformCode": u"",
        u"newEquipmentMOs": []
    },
    u"transCode": u"PTA103"
}

new_equipment = [{
    u"name": u"new device",
    u"quantity": u"1",
    u"purchasePrice": u"100",
    u"registerDate": u"2016-03-30",
    u"actualValue": u"200",
    u"productArea": u"IMPORTED"
}]

party = {
    u"owner": {
        u"name": u"褚修诚",
        u"nature": u"OWNER",
        u"certificateType": u"ID_CARD",
        u"certificateNo": u"44528119801104591X",
        u"mobile": u"",
        u"address": u"北京市朝阳区",
        u"email": u"",
        u"phomeNumber": u"",
        u"vehicleOwnerNature": u"PERSON",
        u"vehicleRelationship": u""
    },
    u"applicant": {
        u"name": u"褚修诚",
        u"nature": u"APPLICANT",
        u"certificateType": u"ID_CARD",
        u"certificateNo": u"44528119801104591X",
        u"mobile": u"",
        u"address": u"北京市朝阳区",
        u"email": u"",
        u"phomeNumber": u"",
        u"vehicleOwnerNature": u"",
        u"vehicleRelationship": u"OWNER"
    },
    u"insured": {
        u"name": u"褚修诚",
        u"nature": u"INSURED",
        u"certificateType": u"ID_CARD",
        u"certificateNo": u"44528119801104591X",
        u"mobile": u"",
        u"address": u"北京市朝阳区",
        u"email": u"",
        u"phomeNumber": u"",
        u"vehicleOwnerNature": u"",
        u"vehicleRelationship": u"OWNER"
    }
}

submit_info = {
    u"requestBodyJson": {
        u"orderNo": u"",
        u"ctpSpecialClauses": [],
        u"bizSpecialClauses": []
    },
    u"transCode": u"TY1003"
}

vehicle_tax = {
      u"taxType": u"",
      u"payStartDate": u"",
      u"payEndDate": u"",
      u"taxAbateType": u"",
      u"taxAbateReason": u"",
      u"taxAbateProportion": u"",
      u"taxAbateAmount": u"",
      u"dutyPaidProofNo": u"",
      u"taxComCode": u"",
      u"taxComName": u""
    }
