# -*- coding: utf-8 -*-
# Created by bida on 2018/11/22
from base64 import b64decode
from io import BytesIO
from time import sleep

import redis
from PIL import Image
from arrow import Arrow
from bs4 import BeautifulSoup
from pytesseract import pytesseract
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select


def validate(captcha):
    if len(captcha) != 4:
        return False

    base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for c in captcha:
        if c not in base:
            return False
    return True


def recognize(screenshot_as_base64):
    try:
        img = Image.open(BytesIO(b64decode(screenshot_as_base64)))
        captcha = pytesseract.image_to_string(img)
        return captcha
    except:
        return ''


def if_alert(driver):
    try:
        driver.switch_to.alert.accept()
    except:
        pass


def get_captcha(driver):
    try:
        driver.switch_to.alert.accept()
    except:
        pass
    screenshot_as_base64 = driver.find_element_by_id('randomImg').screenshot_as_base64
    captcha = recognize(screenshot_as_base64)
    while not validate(captcha):
        driver.find_element_by_id('randomImg').click()
        sleep(1)
        screenshot_as_base64 = driver.find_element_by_id('randomImg').screenshot_as_base64
        captcha = recognize(screenshot_as_base64)
    return captcha


def login(driver):
    driver.get('http://88.32.0.232:88/sinoiais/')
    driver.find_element_by_name('sysUser.userCode').send_keys('PICC3205ztw01')
    sleep(0.1)
    driver.find_element_by_id('passWord').send_keys('369673')

    captcha = get_captcha(driver)
    driver.find_element_by_id('rand').send_keys(captcha)
    sleep(0.1)
    driver.find_element_by_name("login").click()
    sleep(1)

    # success = False if len(driver.find_elements_by_id('randomError')) > 0 else True
    success = False if len(driver.find_elements_by_id('passWord')) > 0 else True

    while not success:
        driver.find_element_by_id('rand').clear()
        driver.find_element_by_id('passWord').send_keys('369673')
        driver.find_element_by_id('randomImg').click()
        sleep(1)
        captcha = get_captcha(driver)
        driver.find_element_by_id('rand').send_keys(captcha)
        sleep(0.1)
        driver.find_element_by_name("login").click()
        sleep(1)
        success = False if len(driver.find_elements_by_id('passWord')) > 0 else True
        # success = False if len(driver.find_elements_by_id('randomError')) > 0 else True



def search_success(driver):
    try:
        alert = driver.switch_to.alert
        alert.accept()
        return False
    except Exception:
        return True


def search(driver, vin):
    if_alert(driver)
    driver.find_element_by_id('vin').clear()
    sleep(0.1)
    driver.find_element_by_id('vin').send_keys(vin)
    sleep(0.1)
    driver.find_element_by_id('randomImg').click()
    sleep(1)

    captcha = get_captcha(driver)
    driver.find_element_by_id('rand').send_keys(captcha)
    sleep(0.5)
    driver.find_element_by_id('but1').click()
    sleep(1)

    success = False if not search_success(driver) else True

    while not success:
        if_alert(driver)
        driver.find_element_by_id('rand').clear()
        sleep(0.2)
        driver.find_element_by_id('randomImg').click()
        sleep(1)
        captcha = get_captcha(driver)
        driver.find_element_by_id('rand').send_keys(captcha)
        sleep(0.5)
        driver.find_element_by_id('but1').click()
        sleep(1)
        success = False if not search_success(driver) else True


def parse(driver, vin):
    soup1 = BeautifulSoup(driver.page_source, 'html.parser')
    div1 = soup1.find_all('div', attrs={'class': 'box'})
    result = ''
    # result += f"{vin}\n"
    v = ''
    for div in div1:
        title = div.find('h1').text
        # result += f"{title}\n"
        div2 = div.find_all('tr', attrs={'class': 'tr1'})
        line = f'{vin},{title}'
        for divb in div2:
            td = divb.find('td')
            if '320017' in td.text or '320018' in td.text:
                items = divb.find_all('td')
                v = items[8].text
                line += f",{','.join([items[8].text, items[0].text, items[4].text, items[5].text])}"
        result += f'{line}\n'
    return result, v


def main(vins):
    chrome_option = Options()
    chrome_option.add_argument('--headless')
    chrome_option.add_argument('--proxy-server=http://10.134.10.9:808')
    chrome_option.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    #
    driver = webdriver.Chrome(executable_path='/Users/bida/Tool/selenium/chromedriver',
                              chrome_options=chrome_option)

    login(driver)

    Select(driver.find_element_by_id('dimensionSelect')).select_by_visible_text('车架号')
    sleep(0.1)
    driver.find_element_by_id('queryMode2').click()
    sleep(0.1)
    driver.find_element_by_id('queryMode4').click()
    sleep(0.1)
    driver.find_element_by_id('queryMode5').click()
    sleep(0.1)
    driver.find_element_by_id('queryMode7').click()
    sleep(0.1)
    driver.find_element_by_id('queryMode8').click()
    sleep(0.1)

    with open(f'{Arrow.now().format("MMDDHHmmss")}.txt', 'w') as f:
        for i in range(len(vins)):
            try:
                search(driver, vins[i])
            except UnexpectedAlertPresentException:
                search(driver, vins[i])
            result, vin = parse(driver, vins[i])
            while vins[i] != vin:
                search(driver, vins[i])
                result, vin = parse(driver, vins[i])
            f.write(result)
            print(f'{Arrow.now().format("HH:mm:ss")} : {i} . {vins[i]} - success')


if __name__ == '__main__':
    vins = ['LSGZJ5353HH053849']
    main(vins)
    # print(validate('abc'))
