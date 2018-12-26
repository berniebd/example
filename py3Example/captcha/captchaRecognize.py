# -*- coding: utf-8 -*-
# Created by bida on 2018/11/21
import base64
from time import sleep

import requests
from PIL import Image
import io
from datetime import datetime
from pytesseract import pytesseract
from selenium import webdriver


def get_timestamp():
    return str(datetime.now().timestamp()).replace('.', '')[:13]


def main():
    header = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Host': '88.32.0.232:88',
        'Origin': 'http://88.32.0.232:88',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://88.32.0.232:88/sinoiais/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    session = requests.Session()
    session.get('http://88.32.0.232:88/sinoiais/', headers=header)
    captcha = ''
    while len(captcha) != 4:
        res1 = session.get(f'http://88.32.0.232:88/sinoiais/pages/login/RandomNumUtil.jsp?d={get_timestamp()}')
        img = Image.open(io.BytesIO(res1.content))
        img.save('1.png')

        captcha = pytesseract.image_to_string(img)
        sleep(1)
    print(captcha)

    res2 = session.post('http://88.32.0.232:88/sinoiais/checklogin/checkLoginInfo.do',
                        data={'sysUserCode': 'PICC3205ztw01', 'sysPassWord': '369673', 'random': captcha},
                        headers=header)
    print(res2.content)

    # driver = webdriver.Chrome()
    # driver.get('http://88.32.0.232:88/sinoiais/')
    # print()


if __name__ == '__main__':
    main()
