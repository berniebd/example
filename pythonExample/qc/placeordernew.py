# -*- encoding:utf-8 -*-
from datetime import datetime
import time
import hashlib
import math
from random import random
from time import sleep
import requests
import simplejson

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

    permanent_id = y + m + d + h + mi + s + ss + cc + b + c
    return permanent_id

def get_timestamep():
    nowtime = datetime.now()
    ss = nowtime.microsecond / 1000
    if ss < 100:
        ss = '00' + str(ss)
    else:
        ss = str(ss)

    return str(int(time.mktime(nowtime.timetuple()))) + ss[len(ss)-3:]

if __name__ == '__main__':
    session = requests.session()
    header = dict()
    header['Cookie'] = '__permanent_id=' + generate_permanent_id() + '; ddscreen=2'
    resp = session.get('http://a.dangdang.com/smart.js?20150611', headers=header)
    timestamp1 = get_timestamep()
    sleep(5);

    header['Cookie'] += '; __ddclick_visit=0000000001.2; __trace_id=' + generate_permanent_id()

    timestamp2 = get_timestamep()

    url = 'https://login.dangdang.com/p/authen_humans_check.php?su_key=bida@dangdang.com&su_do=' + timestamp1 + '&domain=basic_login&jsoncallback=jsonp' + timestamp2

    resp = session.get(url, headers=header, verify=False)
    resp.text

    print resp.text[21:-1]
    jsonp_obj = simplejson.loads(resp.text[21:-1])

    login_data = dict()
    login_data['A12B56CD78EF90G'] = 'Q/BwL8IE66VAqrabWAv56A=='
    login_data['action'] = 'login'
    # login_data['auth_human_id'] = jsonp_obj['person_repid']
    login_data['ispersist'] = 'off'
    login_data['login_type'] = '0'
    login_data['post_type'] = 'normal'
    login_data['returnurl'] = 'http://www.dangdang.com'
    login_data['txtPassword'] = 'bernie0416A'
    login_data['txtUsername'] = 'bida@dangdang.com'
    login_data['txtVerifyCode'] = ''
    login_data['view'] = jsonp_obj['view']
    login_data['wdvalidatetoken'] = 'pMMu1apHz3I='

    resp = session.post('https://login.dangdang.com/signin.php', data=login_data, headers=header, verify=False)

    print resp.text

    handle_addr_data = dict()
    handle_addr_data['addr_detail'] = '朝阳区北三环东路8号静安中心12层'
    handle_addr_data['city_id'] = '1'
    handle_addr_data['country_id'] = '9000'
    handle_addr_data['cust_address_id'] = '19470409'
    handle_addr_data['province_id'] = '111'
    handle_addr_data['quarter_id'] = '111010501'
    handle_addr_data['ship_man'] = 'bernie'
    handle_addr_data['ship_mb'] = '13800138002'
    handle_addr_data['ship_zip'] = '100001'
    handle_addr_data['status'] = '1'
    handle_addr_data['town_id'] = '11101015'

    resp = session.post('http://customer.dangdang.com/myaddress/myaddress_handle.php', data=handle_addr_data)
    print resp.text
