# -*- encoding:utf-8 -*-
import os

import dicttoxml
from lxml import etree as ET

import cx_Oracle

__author__ = 'bida'

req_xml = '''
<?xml version="1.0" encoding="UTF-8"?>
<request>
    <head>
        <partnerCode>SAIC</partnerCode>
        <transactionCode>106004</transactionCode>
        <messageId>BK16000225143r6lJDQJ</messageId>
        <transactionEffectiveDate>2016-09-29 18:07:08</transactionEffectiveDate>
        <user>SAIC</user>
        <password>UJNR/UNX9u7FiBqfaSRyoEiuOkHWbmbQQbOUOi6vNXn9B+ZeA2Z0INZlMv0DU+zGjI4GgC2UTPOOl/zJGPjpAQ==</password>
    </head>
    <body>
    <QueryPolicyRequest>
        <branchCode>3070100</branchCode>
        <applicationNo>AFUZ001Y1416A000182H</applicationNo>
        <terminalNo>VW860001</terminalNo>
    </QueryPolicyRequest>
    </body>
</request>
'''


def query_biz_or_ctp_application_cpic(req):
    # print(type(req_xml))
    # req = ET.fromstring(str(req_xml).strip().encode())
    # req = ET.fromstring(req_xml)

    response = {'response': {
        'head': {},
        'body': {'QueryPolicyResponse': {}}
    }}

    head = response['response']['head']

    head['partnerCode'] = req.xpath('//request/head/partnerCode')[0].text
    head['transactionCode'] = req.xpath('//request/head/transactionCode')[0].text
    head['messageId'] = req.xpath('//request/head/messageId')[0].text
    head['transactionEffectiveDate'] = req.xpath('//request/head/transactionEffectiveDate')[0].text
    head['responseCompleteMessageStatus'] = {}
    head['responseCompleteMessageStatus']['messageStatusCode'] = '000000'
    head['responseCompleteMessageStatus']['messageStatusDescriptionNumber'] = '0'

    queryPolicyResponse = response['response']['body']['QueryPolicyResponse']

    queryPolicyResponse['branchCode'] = req.xpath('//body/QueryPolicyRequest/branchCode')[0].text
    queryPolicyResponse['applicationNo'] = req.xpath('//body/QueryPolicyRequest/applicationNo')[0].text

    order_no = req.xpath('//request/head/messageId')[0].text[:12]
    applicant_no = req.xpath('//request/body/QueryPolicyRequest/applicationNo')[0].text
    print(order_no)

    os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
    with cx_Oracle.connect('monitor', 'monitor', '10.118.22.40:1521/sudbte') as conn:
        cur = conn.cursor()

        queryPolicyResponse['policyNo'] = req.xpath('//body/QueryPolicyRequest/applicationNo')[0].text
        queryPolicyResponse['applicationStatus'] = req.xpath('//body/QueryPolicyRequest/applicationNo')[0].text
        queryPolicyResponse['policyStatus'] = req.xpath('//body/QueryPolicyRequest/applicationNo')[0].text

        sql = "SELECT pp.NAME FROM POLICYOWNER.PS_PARTY pp WHERE pp.ORDER_NO = '{}' AND pp.nature = 'APPLICANT'".format(
            order_no)
        cur.execute(sql)
        applicant = cur.fetchall()
        queryPolicyResponse['applicant'] = applicant[0][0]

        sql = "SELECT pp.NAME,pp.MOBILE FROM POLICYOWNER.PS_PARTY pp WHERE pp.ORDER_NO = '{}' AND pp.nature = 'INSURED'".format(
            order_no)
        cur.execute(sql)
        insured = cur.fetchall()
        queryPolicyResponse['insured'] = insured[0][0]
        queryPolicyResponse['insuredPhone'] = insured[0][1]

        sql = "SELECT pv.LICENSE_NO,pv.LICENSE_COLOR,pv.VIN,pv.ENGINE_NO " \
              "FROM policyowner.PS_VEHICLE pv WHERE pv.ORDER_NO = '{}'".format(order_no)
        cur.execute(sql)
        vehicle = cur.fetchall()
        queryPolicyResponse['plateNo'] = vehicle[0][0]
        queryPolicyResponse['plateColor'] = vehicle[0][1]
        queryPolicyResponse['engineNo'] = vehicle[0][2]
        queryPolicyResponse['carVIN'] = vehicle[0][3]

        sql = "SELECT pp.INS_AGENT_CODE,pp.START_DATE,pp.END_DATE,pp.ACTUAL_PREMIUM,pp.SUMINSURED," \
              "TO_CHAR(pp.ENFORCE_TIME,'yyyy-mm-dd HH24:mi:ss') FROM POLICYOWNER.PS_POLICY pp " \
              "WHERE pp.ORDER_NO = '{0}' AND pp.APPLICATION_NO = '{1}'".format(order_no, applicant_no)
        cur.execute(sql)
        policy = cur.fetchall()

        queryPolicyResponse['agencyId'] = policy[0][0]
        queryPolicyResponse['efficientDate'] = policy[0][1]
        queryPolicyResponse['terminationDate'] = policy[0][2]
        queryPolicyResponse['premium'] = '%.2f' % (policy[0][3])
        queryPolicyResponse['sumasSured'] = '%.2f' % (policy[0][4])
        queryPolicyResponse['inputTime'] = policy[0][5]
        queryPolicyResponse['createDate'] = policy[0][5]
        queryPolicyResponse['enforceDate'] = policy[0][5]

        sql = "SELECT po.PAY_NO FROM POLICYOWNER.PS_ORDER po WHERE po.ORDER_NO = '{0}'".format(order_no)
        cur.execute(sql)
        order = cur.fetchall()
        queryPolicyResponse['payappNo'] = order[0][0].split('-')[0]

        queryPolicyResponse['inputorId'] = 'KSM349'
        queryPolicyResponse['agentId'] = '999'
        queryPolicyResponse['deptGroupCode'] = '350100'
        queryPolicyResponse['deptCode'] = '001'
        queryPolicyResponse['sectionCode'] = '982'
        queryPolicyResponse['feeStatus'] = '2'
        queryPolicyResponse['CheckCode'] = '9674'
        queryPolicyResponse['UWResult'] = {}
        queryPolicyResponse['UWResult']['uwResult'] = '2'
        queryPolicyResponse['UWResult']['violationRules'] = '核保通过'

    xml_res = dicttoxml.dicttoxml(response, attr_type=False)
    return xml_res.decode()


if __name__ == '__main__':
    req = ET.fromstring(str(req_xml).strip().encode())
    print(query_biz_or_ctp_application_cpic(req))
