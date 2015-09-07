# -*- encoding:utf-8 -*-
import requests
import simplejson

session = requests.session()
print '*' * 20 + '登陆当当'
login_data = dict()
login_data['action'] = 'login'
login_data['ispersist'] = 'off'
login_data['login_type'] = '0'
login_data['post_type'] = 'normal'
login_data['returnurl'] = 'http://www.dangdang.com'
login_data['txtPassword'] = 'bernie0416A'
login_data['txtUsername'] = 'bida@dangdang.com'

resp = session.post('https://login.dangdang.com/signin.php', data=login_data, verify=False)
print len(session.cookies)
print type(session.cookies)
for item in session.cookies.items():
    print item
    print type(item)
    print item[1]
print '*' * 20 + '修改地址'
handle_addr_data = dict()
handle_addr_data['addr_detail'] = '第五广场C座8层'
handle_addr_data['city_id'] = '1'
handle_addr_data['country_id'] = '9000'
handle_addr_data['cust_address_id'] = '19470409'
handle_addr_data['province_id'] = '111'
handle_addr_data['quarter_id'] = '111010501'
handle_addr_data['ship_man'] = 'bernie'
handle_addr_data['ship_mb'] = '13800138004'
handle_addr_data['ship_zip'] = '100001'
handle_addr_data['status'] = '1'
handle_addr_data['town_id'] = '1110101'

# resp = session.post('http://customer.dangdang.com/myaddress/myaddress_handle.php', data=handle_addr_data)

# print '*' * 20 + '添加至购物车'
# session.get('http://shopping.dangdang.com/shoppingcart/shopping_cart_add.aspx?product_ids=25005604')
#
# print '*' * 20 + '结算'
# resp = session.get('http://checkout.dangdang.com/checkout.aspx#dd_refer=http%3A%2F%2Fshopping.dangdang.com%2Fshoppingcart%2Fshopping_cart.aspx')
# # print resp.text
# #
# resp = session.post('http://checkout.dangdang.com/order_flow_checker.aspx')
print resp.text
# #
# resp = session.post('http://checkout.dangdang.com/order_flow.aspx')
# print resp.text
# #
# resp = session.post('http://checkout.dangdang.com/order_flow_submit.aspx')
# print resp.text
# #
# preorder_obj = simplejson.load(resp.text)
# url = 'http://cashier.dangdang.com/cashier.aspx?grand_order_id=' + preorder_obj['grand_order_id'] + '&pre_submit_count=0&order_type=0'
# submit_data = dict()
# submit_data['dq_status'] = 'underfined'
# submit_data['input_charset'] = 'underfined'
# submit_data['is_package_order'] = '0'
# submit_data['order_info'] = 'underfined'
# submit_data['order_type'] = 'underfined'
# submit_data['parent_id'] = 'underfined'
# submit_data['partner_id'] = 'underfined'
# submit_data['pay_from'] = 'underfined'
# submit_data['pay_id'] = 'underfined'
# submit_data['pay_type'] = 'underfined'
# submit_data['pick_up_id'] = 'underfined'
# submit_data['pre_submit_order_count'] = 'underfined'
# submit_data['product_ids'] = 'underfined'
# submit_data['ship_type'] = 'underfined'
# submit_data['shop_id'] = 'underfined'
# submit_data['sign'] = 'underfined'
#
# resp = session.post(url, data=submit_data)
# print resp.text
