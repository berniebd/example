# -*- coding: utf-8 -*-
# Created by bida on 2018/12/17
import requests
from bs4 import BeautifulSoup

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': 'read_mode=day; default_font=font2; locale=zh-CN; __yadk_uid=XEmf9k8RwNQG7FdEv1AEhR3DkKeb8bVq; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1545035165,1545037890,1545037956,1545037971; _m7e_session=ed73e862e6ea6181d6174dcf750288ea; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2215475806%22%2C%22%24device_id%22%3A%221675e25841c6e-0b8a3512b94f41-35677607-2073600-1675e25841d140%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%221675e25841c6e-0b8a3512b94f41-35677607-2073600-1675e25841d140%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1545039492',
    'Host': 'www.jianshu.com',
    'If-None-Match': 'W/"c3d622e8acd2a70e18be4078cf2be4d0"',
    'Referer': 'https://www.jianshu.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
}
resp = requests.get('https://www.jianshu.com/p/066236b855dc', headers=headers).content

html = BeautifulSoup(resp, 'html.parser', from_encoding='utf-8')
html.select
reward = html.find('div', attrs={'id': 'free-reward-panel'})
print()
