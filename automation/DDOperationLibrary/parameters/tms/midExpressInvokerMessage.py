# -*- encoding:utf-8 -*-
__author__ = 'bida'

xml = '<?xml version="1.0" encoding="utf-8" standalone="yes" ?><inputObject><list>${rows}</list></inputObject>'

in_store_item = '<row><order_id>${order_id}</order_id><in_storage_date>2015-11-22 11:41:53</in_storage_date><express_id>${express_id}</express_id><operator>【冯哥】</operator></row>'

out_store_item = '<row><order_id>${order_id}</order_id><out_storage_date>2015-11-22 11:41:53</out_storage_date><express_operator_name>【02透笼站】【】</express_operator_name><express_operator_tel>【冯哥】【18846109717】</express_operator_tel><express_operator_id>1312</express_operator_id><express_id>${express_id}</express_id><operator>透笼</operator></row>'

feedback_result_item = '<row><order_id>${order_id}</order_id><sign_date>2015-11-22 11:41:53</sign_date><sign_person>张三</sign_person><order_status>${order_status}</order_status><reason>${reason_id}</reason><express_id>${express_id}</express_id><operator>【冯哥】</operator></row>'

feedback_logistic_log_item = '<row><order_id>${order_id}</order_id><trans_log>【经到达**站，查询电话***—********】</trans_log><log_time>2015-11-22 11:41:53</log_time><express_id>${express_id}</express_id><operator>【冯哥】</operator></row>'
