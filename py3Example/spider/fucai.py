# -*- coding: utf-8 -*-
# Created by bida on 2018/7/26
import sqlite3

import requests

def crawl():
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Host': 'www.cwl.gov.cn',
        'Referer': 'http://www.cwl.gov.cn/kjxx/ssq/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    session = requests.Session()
    url = 'http://www.cwl.gov.cn/cwl_admin/kjxx/findKjxx/forIssue?name=ssq&code={0}{1}{2}'
    for year in range(2017, 2019):
        for period in range(140, 160):
            resp = session.get(url.format(year, '0'*(3-len(str(period))), period), headers=headers)
            if resp.json()['state'] == 1:
                break
            print(resp.json())

if __name__ == '__main__':
    conn = sqlite3.connect('fucai.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS RECORD(CODE TEXT, DDATE TEXT)')
    crawl()