# -*- coding: utf-8 -*-
# Created by bida on 2018/11/22
from bs4 import BeautifulSoup

soup1 = BeautifulSoup(open('/Users/bida/Desktop/123html.html'), 'html.parser')
div1 = soup1.find_all('div', attrs={'class': 'box'})
with open('result.txt', 'w') as f:
    for div in div1:
        f.write(div.find('h1').text)
        f.write('\n')
        div2 = div.find_all('tr', attrs={'class': 'tr1'})
        for divb in div2:
            td = divb.find('td')
            if '320017' in td.text or '320018' in td.text:
                items = divb.find_all('td')
                f.write(','.join([items[0].text, items[4].text, items[5].text]))
                f.write('\n')
