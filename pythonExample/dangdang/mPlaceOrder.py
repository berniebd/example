# -*- encoding:utf-8 -*-
import re
import requests
import simplejson

__author__ = 'bida'

session = requests.session()
print '*' * 20 + '登录'
resp = session.post("http://passport.m.dangdang.com/login.php", data={'username': '18600365141', 'password': ''})
print resp.text
obj = simplejson.loads(resp.text)
token_id = obj['userinfo']['token_id']
mdd_code = obj['userinfo']['mdd_code']
sid = obj['sid']
print '*' * 20 + '添加至购物车'
resp = session.get('http://product.m.dangdang.com/h5ajax.php?action=cart_append_products&product_ids=23687172.1&sid=' + sid)
# print resp.text

# resp = session.get('http://product.m.dangdang.com/h5ajax.php?action=cart_product_total&sid=' + sid)
# # print resp.text
#
# resp = session.get('http://m.dangdang.com/touch/cart.php?action=list_cart&sid=' + sid)
# # print resp.text
#
# pattern = re.compile(r'input type="hidden" value="(.*)" name="timestamp')
# res = pattern.search(resp.text).groups()
# print res[0]
# timestamp = res[0]
#
# pattern = re.compile(r'input type="hidden" value="(.*)" name="permanent_id')
# res = pattern.search(resp.text).groups()
# print res[0]
# permanent_id = res[0]
#
# pattern = re.compile(r'input type="hidden" value="(.*)" name="time_code')
# res = pattern.search(resp.text).groups()
# print res[0]
# time_code = res[0]
#
# data = dict()
# data['action'] = 'get_order_flow'
# data['client_version'] = '1.0'
# data['permanent_id'] = permanent_id
# data['ref'] = 'ckadd'
# data['shop_id'] = '0'
# data['time_code'] = time_code
# data['timestamp'] = timestamp
# data['udid'] = sid
# data['union_id'] = ''
# data['user_client'] = 'touch'
# print data
# resp = session.post('http://mcheckout.dangdang.com/h5_checkout.php', data=data)
# print resp.text
