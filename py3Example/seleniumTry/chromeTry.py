# -*- coding: utf-8 -*-
# Created by bida on 2018/8/30
from concurrent import futures
from threading import Thread

from arrow import Arrow
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options

def tt(i):
    chrome_option = Options()
    # chrome_option.add_argument('--headless')
    chrome_option.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    #
    # driver = webdriver.Chrome(executable_path='/Users/bida/Tool/selenium/chromedriver',
    #                           chrome_options=chrome_option)
    # driver.get('https://list.jd.com/list.html?cat=652,654,832https://www.baidu.com')
    #
    # driver.get_screenshot_as_file('1.png')


    driver2 = webdriver.Remote(command_executor='http://192.168.2.1:4444/wd/hub',
                               desired_capabilities=DesiredCapabilities.CHROME,
                               options=chrome_option)
    driver2.get('http://www.baidu.com')

    png = driver2.find_element_by_id('s_lg_img').screenshot_as_base64
    print(f'{i}: {Arrow.now().format("HH:mm:ss.SSS")}')
    driver2.save_screenshot(f'{i}.png')
    driver2.quit()

if __name__ == '__main__':
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(tt, range(10))
