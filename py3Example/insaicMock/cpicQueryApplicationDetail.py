# -*- encoding:utf-8 -*-
__author__ = 'bida'

import dicttoxml
from lxml import etree as ET

import cx_Oracle

__author__ = 'bida'

req_xml = '''
<?xml version="1.0" encoding="UTF-8"?>
<request>
    <head>
        <partnerCode>SAIC</partnerCode>
        <transactionCode>106012</transactionCode>
        <messageId>BK1600022514gjNAbrYq</messageId>
        <transactionEffectiveDate>2016-09-29 18:07:08</transactionEffectiveDate>
        <user>SAIC</user>
        <password>UJNR/UNX9u7FiBqfaSRyoEiuOkHWbmbQQbOUOi6vNXn9B+ZeA2Z0INZlMv0DU+zGjI4GgC2UTPOOl/zJGPjpAQ==</password>
    </head>
    <body>
    <QueryPolicyDetailRequest>
        <policyNo></policyNo>
        <applicationNo>AFUZ001Y1416A000182H</applicationNo>
        <agentCode>0TD</agentCode>
    </QueryPolicyDetailRequest>
    </body>
</request>
'''

temp_res = '''
<?xml version='1.0' encoding='UTF-8'?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
	<soapenv:Body>
		<ns:queryVehicleModelResponse xmlns:ns="http://service.front.sinosoft.com">
			<ns:return xmlns:ax213="http://busInterface.front.sinosoft.com/xsd" xmlns:ax215="http://dto.front.sinosoft.com/xsd" xmlns:ax216="http://common.dto.front.sinosoft.com/xsd" xmlns:ax219="http://out.vehicleModelQuery.dto.front.sinosoft.com/xsd" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="ax215:VehicleModelQueryResponse">
				<ax215:policySort>EA3</ax215:policySort>
				<ax215:txInsuranceResponseEhm xsi:type="ax216:TxInsuranceResponseEhm">
					<ax216:transExeDate xsi:nil="true"/>
					<ax216:transExeTime xsi:nil="true"/>
					<ax216:transRefGUID xsi:nil="true"/>
					<ax216:transSubType xsi:nil="true"/>
					<ax216:transType xsi:nil="true"/>
					<ax216:oinsuranceExtensionEhm xsi:type="ax216:OinsuranceExtensionEhm">
						<ax216:maxRecords>0</ax216:maxRecords>
					</ax216:oinsuranceExtensionEhm>
					<ax216:transResultEhm xsi:type="ax216:TransResultEhm">
						<ax216:errorNo/>
						<ax216:errorType xsi:nil="true"/>
						<ax216:resultCode>1</ax216:resultCode>
						<ax216:resultInfoDesc>服务调用成功</ax216:resultInfoDesc>
						<ax216:stackTrace xsi:nil="true"/>
					</ax216:transResultEhm>
				</ax215:txInsuranceResponseEhm>
				<ax215:txInsuranceResponseExtensionEhm xsi:type="ax216:TxInsuranceResponseExtensionEhm">
					<ax216:operator xsi:nil="true"/>
					<ax216:operatorKey xsi:nil="true"/>
				</ax215:txInsuranceResponseExtensionEhm>
				<ax215:vehicleModelDataArr xsi:type="ax219:VehicleModelData">
					<ax219:exhaustScale>2.997</ax219:exhaustScale>
					<ax219:fuelCode/>
					<ax219:fuelName/>
					<ax219:fuleType xsi:nil="true"/>
					<ax219:importFlag>C</ax219:importFlag>
					<ax219:marketDate>201312</ax219:marketDate>
					<ax219:modelCode>BKAAND0079</ax219:modelCode>
					<ax219:platModelCode>BTYPJZUD0028</ax219:platModelCode>
					<ax219:platModelName>别克SGM7300EAAB 智享旗舰型</ax219:platModelName>
					<ax219:purchasePrice>317900.0</ax219:purchasePrice>
					<ax219:seatCount>5</ax219:seatCount>
					<ax219:standardName>别克SGM7300EAAB轿车</ax219:standardName>
					<ax219:tonCount>0.0</ax219:tonCount>
					<ax219:vehicleWeight>1850.0</ax219:vehicleWeight>
				</ax215:vehicleModelDataArr>
			</ns:return>
		</ns:queryVehicleModelResponse>
	</soapenv:Body>
</soapenv:Envelope>
'''


def query_application_detail(req):
    response = {'response': {
        'head': {},
        'body': {'QueryPolicyDetailResponse': {}}
    }}

    head = response['response']['head']

    head['partnerCode'] = req.xpath('//request/head/partnerCode')[0].text
    head['transactionCode'] = req.xpath('//request/head/transactionCode')[0].text
    head['messageId'] = req.xpath('//request/head/messageId')[0].text
    head['transactionEffectiveDate'] = req.xpath('//request/head/transactionEffectiveDate')[0].text
    head['responseCompleteMessageStatus'] = {}
    head['responseCompleteMessageStatus']['messageStatusCode'] = '000000'
    head['responseCompleteMessageStatus']['messageStatusDescriptionNumber'] = '0'

    applicant = response['response']['body']['QueryPolicyDetailResponse']['Applicant']

    xml_res = dicttoxml.dicttoxml(response, root=False, attr_type=False)
    return xml_res.decode()


if __name__ == '__main__':
    req = ET.fromstring(str(req_xml).strip().encode())
    print(query_application_detail(req))
