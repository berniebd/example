# -*- encoding:utf-8 -*-
from flask import Flask, request
from lxml import etree

from insaicMock.cpicQueryBizOrCtpApplication import query_biz_or_ctp_application_cpic
from insaicMock.cpicQueryVehicleModel import query_vehicle_model

__author__ = 'bida'

app = Flask(__name__)


@app.route('/cpic', methods=['POST'])
def cpic():
    req_data = request.get_data()

    req = etree.fromstring(req_data)
    transaction_code = req.xpath('//request/head/transactionCode')[0].text

    res_data = ''
    if transaction_code == '106001':
        res_data = query_vehicle_model(req)
    if transaction_code == '106004':
        res_data = query_biz_or_ctp_application_cpic(req)
    return res_data


if __name__ == '__main__':
    app.run(debug=True)