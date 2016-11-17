# -*- encoding:utf-8 -*-
import mysql.connector
from lxml import etree as ET
import dicttoxml

__author__ = 'bida'

req = '''
<?xml version="1.0" encoding="UTF-8"?>
<request>
    <head>
        <partnerCode>SAIC</partnerCode>
        <transactionCode>106001</transactionCode>
        <messageId>BK1600022514PhLl2WGm</messageId>
        <transactionEffectiveDate>2016-09-29 17:45:54</transactionEffectiveDate>
        <user>SAIC</user>
        <password>UJNR/UNX9u7FiBqfaSRyoEiuOkHWbmbQQbOUOi6vNXn9B+ZeA2Z0INZlMv0DU+zGjI4GgC2UTPOOl/zJGPjpAQ==</password>
    </head>
    <body>
    <QueryVehicleModelRequest>
        <vehicleName>别克SGM7146TATB轿车</vehicleName>
        <productKind>AUTOCOMPRENHENSIVEINSURANCE2014PRODUCT</productKind>
        <pageNum>1</pageNum>
        <terminalNo>VW860001</terminalNo>
        <moldCharacterCode>BKAARD0006</moldCharacterCode>
    </QueryVehicleModelRequest>
    </body>
</request>
'''

def query_vehicle_model(req):
    # req = ET.fromstring(req_xml.strip().encode())
    req_head = req.find('head')

    response = {'response': {
        'head': {},
        'body': {
            'QueryVehicleModelResponse': {
                'VehicleModelList': {},
                'deductionDueTaxDate': '2015-09-11'
            }}
    }}

    head = response['response']['head']
    head['partnerCode'] = req_head.find('partnerCode').text
    head['transactionCode'] = req_head.find('transactionCode').text
    head['messageId'] = req_head.find('messageId').text
    head['transactionEffectiveDate'] = req_head.find('transactionEffectiveDate').text
    head['responseCompleteMessageStatus'] = {}
    head['responseCompleteMessageStatus']['messageStatusCode'] = '000000'
    head['responseCompleteMessageStatus']['messageStatusDescriptionNumber'] = '0'
    config = {'user': 'insaic', 'password': 'insaic', 'host': '10.118.22.33', 'database': 'insaic'}

    cnx = cur = None
    cnx = mysql.connector.connect(**config)
    cur = cnx.cursor()
    sql = '''
        select model_code,model_name,series_name,remark,car_year,purchase_price,seat_count,completemass,exhaust_scale,
            brand_name,producing_area,risk_type,tpy_risk_type,vehicle_code_hy,vehicle_name_hy,deduction_due_code_jy,
            fuel_type_jy from vehicle_model
    '''
    cur.execute(sql)
    vechile = cur.fetchall()[0]

    vehicle_model_list = response['response']['body']['QueryVehicleModelResponse']['VehicleModelList']
    vehicle_model_list['moldCharacterCode'] = vechile[0].decode()
    vehicle_model_list['vehicleFamily'] = vechile[2].decode()
    vehicle_model_list['vehicleDescription'] = vechile[3].decode()
    vehicle_model_list['marketDate'] = vechile[4].decode()
    vehicle_model_list['purchasePrice'] = vechile[5]
    vehicle_model_list['seatCount'] = vechile[6]
    vehicle_model_list['emptyWeight'] = vechile[7]
    vehicle_model_list['engineCapacity'] = vechile[8]
    vehicle_model_list['vehicleBrand'] = vechile[9].decode()
    vehicle_model_list['makerModel'] = vechile[1].decode()
    vehicle_model_list['producingArea'] = vechile[10].decode()
    vehicle_model_list['riskFlagCode'] = vechile[11].decode()
    vehicle_model_list['tpyRiskflagCode'] = vechile[12].decode()
    vehicle_model_list['vehicleHyCode'] = vechile[13].decode()
    vehicle_model_list['vehicleHyName'] = vechile[15].decode()
    vehicle_model_list['DeductionDueCodeJY'] = vechile[15].decode()
    vehicle_model_list['FuelTypeJY'] = vechile[16].decode()

    xml_res = dicttoxml.dicttoxml(response, attr_type=False)
    print(xml_res.decode())

    cur.close()
    cnx.close()

    return xml_res.decode()
