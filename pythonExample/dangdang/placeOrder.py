# -*- encoding:utf-8 -*-
from datetime import datetime
import hashlib
import math
from random import random
import re
import requests

__author__ = 'bida'

ddclick_hash_key = 'DDClick521'

def generate_permanent_id():
    nowtime = datetime.now()
    y = str(nowtime.year)
    if nowtime.month < 10:
        m = '0' + str(nowtime.month)
    else:
        m = str(nowtime.month)
    if nowtime.day < 10:
        d = '0' + str(nowtime.day)
    else:
        d = str(nowtime.day)
    if nowtime.hour < 10:
        h = '0' + str(nowtime.hour)
    else:
        h = str(nowtime.hour)
    if nowtime.minute< 10:
        mi = '0' + str(nowtime.minute)
    else:
        mi = str(nowtime.minute)
    if nowtime.second < 10:
        s = '0' + str(nowtime.second)
    else:
        s = str(nowtime.second)
    ss = nowtime.microsecond / 1000;
    if ss < 100:
        ss = '00' + str(ss)
    else:
        ss = str(ss)
    ss = ss[len(ss)-3:]

    b = str(int(math.floor(100000 + random() * 900000)))
    c = str(int(math.floor(100000 + random() * 900000)))

    f = hashlib.md5()
    f.update(y + m + d + h + mi + s + ss + b + c + ddclick_hash_key)
    md5_hex = f.hexdigest()

    cc = str(int(md5_hex[0:8], 16))[0:6]
    cc = '0' * (6 - len(cc)) + cc

    content = y + m + d + h + mi + s + ss + cc + b + c
    return content

def get_re_value(expression, content):
    pattern = re.compile(expression)
    res = pattern.search(content).groups()
    return res[0]

if __name__ == '__main__':
    session = requests.session()
    permanent_id = generate_permanent_id()
    header = dict()
    print '*' * 30
    header['Cookie'] = '__permanent_id=' + permanent_id + '; ddscreen=2'
    resp = session.get('http://a.dangdang.com/getJS.php?cpc=true&cpm=true&cpt=true', headers=header)
    print len(session.cookies)

    print '*' * 30
    trace_id = generate_permanent_id()
    header['Cookie'] = '__permanent_id=' + permanent_id + '; ddscreen=2; __ddclick_visit=0000000001.1; __trace_id=' + trace_id + ';'
    resp = session.get('http://www.dangdang.com/get_personal_data_2014.php?area_num=0&type=screen_one&t=0.015813458746119946',
                       headers=header)
    print len(session.cookies)

    print '*' * 30
    resp = session.get('https://login.dangdang.com/signin.aspx?returnurl=http%3A//www.dangdang.com/', verify=False)
    post_type = get_re_value('hidden" id="post_type" name="post_type" value="(.*)"/>', resp.text)
    view = get_re_value('hidden" name="view"   id="view"  value="(.*)"/>', resp.text)
    A12B56CD78EF90G = get_re_value('id="A12B56CD78EF90G" name="A12B56CD78EF90G"  value="(.*)" />', resp.text)
    wdvalidatetoken = get_re_value('id="wdvalidatetoken" name="wdvalidatetoken"  value="(.*)" />', resp.text)
    auth_human_id = get_re_value('id="auth_human_id" name="auth_human_id"  value="(.*)" />', resp.text)

    data = dict()
    data['A12B56CD78EF90G'] = A12B56CD78EF90G
    data['action'] = 'login'
    data['auth_human_id'] = auth_human_id
    data['ispersist'] = 'off'
    data['login_type'] = '0'
    data['post_type'] = 'normal'
    data['returnurl'] = 'http://www.dangdang.com'
    data['txtPassword'] = 'bernie0416A'
    data['txtUsername'] = 'bida@dangdang.com'
    data['txtVerifyCode'] = ''
    data['view'] = view
    data['wdvalidatetoken'] = wdvalidatetoken

    resp = session.post('https://login.dangdang.com/signin.php', verify=False, data=data)
    # print resp.text
    # print len(session.cookies)
    # print len(resp.cookies)

    print '*' * 30 + '添加购物车'
    resp = session.get('http://shopping.dangdang.com/shoppingcart/shopping_cart_add.aspx?product_ids=25005604', headers=header)
    resp = session.get('http://shopping.dangdang.com/shoppingcart/shopping_cart', headers=header)
    print type(session.cookies)
    print len(session.cookies)
    print session.cookies.get('JSESSIONID')
    for item in session.cookies.items():
        # print item
        header['Cookie'] += item[0] + '=' + item[1] + ';'
    header['Cookie'] += 'cart_id=200000000607062;cart_items_count=1;'

    print header
    url = 'http://checkout.dangdang.com/checkout.aspx#dd_refer=http%3A%2F%2Fshopping.dangdang.com%2Fshoppingcart%2Fshopping_cart%3Bjsessionid%' + session.cookies.get('JSESSIONID')
    resp = session.get(url, headers=header)

    resp = session.post('http://checkout.dangdang.com/order_flow_checker.aspx')
    print resp.text

