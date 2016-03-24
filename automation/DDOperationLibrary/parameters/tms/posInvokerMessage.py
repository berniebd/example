# -*- encoding:utf-8 -*-
__author__ = 'bida'

tms_pos_exceptional_delivery = '''
{"messageType": "TMS_POS_EXP_TNT","body": "{'orderNo':'${order_no}','exCode':'$[exCode}','exDesc':'斯蒂芬hi阿斯兰的放假阿斯兰发','deliveryMan':'00000001', 'deliveryName':'李四'}","dest": "OC","sendTime": "2016-01-12 14:10:51","src": "IT","messageId": "161af185-ab53-4146-861e-e0d09415818d","messageProcessorName": null}
'''

tms_pos_payment_reverse = '''
{"messageType": "TMS_POS_REVERSE_TNT","body": "{'payType':'${pay_type}','reverseAmt':${reverse_amt},'reverseTranType':'${reverse_type}','orderNo':'${order_no}','idTxn':'336271420','terminalId':'05020667','reverseTraceNo':'014049','deliveryMan':'00000001', 'deliveryName':'李四'}","dest": "OC","sendTime": "2016-01-08 10:24:02","src": "IT","messageId": "72b9ddf4-8909-42fc-96e5-251e4bd717b3","messageProcessorName": null}
'''

tms_pos_signment_feedback = '''
{"messageType": "POS_PAID_TNT","body": "{'orderNo':'${order_no}','signee':'张三','consigneeSignFlag':'Y','deliveryMan':'00000001', 'deliveryName':'李四'}","dest": "OC","sendTime": "2015-12-18 16:55:27","src": "IT","messageId": "9cde8be4-54a5-4dde-a385-453f09c2881a","messageProcessorName": null}
'''

tms_pos_cancel_payment = '''
{"messageType":"CL_POS_PAID_TNT","body":"{'orderNo':'${order_no}','idTxn':'28934718923789127391237891239','voidTraceNo':'342343234234','deliveryMan':'00000001', 'deliveryName':'李四'}","dest":"OC","sendTime":"2015-12-18 15:17:43","src":"IT","messageId":"066114e3-d4ec-4737-a122-65cbf9dc350d","messageProcessorName":null}
'''

tms_pos_payment_feedback = '''
{"messageType": "TMS_POS_PAID_TNT","body": "{'orderNo':'${order_no}','orderPayableAmt':${order_payable_amount},'payType':'${pay_type}','terminalId':'12312312312','signee':null,'idTxn':'28934718923789127391237891239','traceNo':'342343234234','consigneeSignFlag':null,'deliveryMan':'00000001', 'deliveryName':'李四'}","dest": "BMS","sendTime": "2015-12-18 10:58:23","src": "OC","messageId": "59393cdb-4a97-47ae-a46c-5f949f1b6885","messageProcessorName": null}
'''