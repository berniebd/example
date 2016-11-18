# -*- encoding:utf-8 -*-
__author__ = 'bida'

express_feedback_instock_item = '''
{'express_id':'${express_id}','order_id': '${order_id}','express_operator_name':'张三','express_operator_tel':'13800138000','express_operator_id':'123456','operator':'operator'}
'''

express_feedback_instock = '''
{"messageType": "_3PL_INBOUND_TNT","body": "[${items}]","dest": "OC","sendTime": "2015-12-18 16:55:27","src": "EXPRESS","messageId": "9cde8be4-54a5-4dde-a385-453f09c2881a","messageProcessorName": null}
'''

express_feedback_out_of_stock_item = '''
{'express_id':'${express_id}','order_id': '${order_id}','express_operator_name':'张三','express_operator_tel':'13800138000','express_operator_id':'123456','operator':'operator'}
'''

express_feedback_out_of_stock = '''
{"messageType": "_3PL_OUTBOUNT_TNT","body": "[${items}]","dest": "OC","sendTime": "2015-12-18 16:55:27","src": "EXPRESS","messageId": "9cde8be4-54a5-4dde-a385-453f09c2881a","messageProcessorName": null}
'''

express_feedback_delivery_result_item = '''
{'express_id':'${express_id}','order_id':'${order_id}','order_status':'${feedback_status}','reason':'${reason}','sign_date':'2015-12-18 16:55:27','sign_person':'张三','operator':'operator人'}
'''

express_feedback_delivery_result = '''
{"messageType": "_3PL_RESULT_TNT","body": "[${items}]","dest": "OC","sendTime": "2015-12-18 16:55:27","src": "EXPRESS","messageId": "9cde8be4-54a5-4dde-a385-453f09c2881a","messageProcessorName": null}
'''

express_feedback_logistics_log_item = '''
{'express_id':'${express_id}','order_id':'${order_id}','trans_log':'快递反馈物流日志','log_time':'2015-12-18 16:55:27','operator':'operator'}
'''

express_feedback_logistics_log = '''
{"messageType": "_3PL_LOG","body": "[${items}]","dest": "OC","sendTime": "2015-12-18 16:55:27","src": "EXPRESS","messageId": "9cde8be4-54a5-4dde-a385-453f09c2881a","messageProcessorName": null}
'''
