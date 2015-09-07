# encoding=utf-8
from lxml import etree

__author__ = 'bida'

import requests

session = requests.session()

session.post('http://ehr.dangdang.com/templates/index/hrlogon.do',
             data={'logon.x': 'link', 'username': 'bida', 'password': 'bernie0416A'})

resp = session.post('http://ehr.dangdang.com/kq/kqself/card/carddata.do?b_query=link',
                    data={'start_date': '2015.06.01', 'end_date': '2015.06.30', 'listpagination': 'baseNetSignInForm', 'current': '1'})
print resp.text
object = etree.fromstring(resp.text)
print object




