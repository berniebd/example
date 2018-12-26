# -*- coding: utf-8 -*-
# Created by bida on 2018/12/18
import random
from time import sleep

import requests
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def get_url():
    return requests.get(
        url='http://10.118.22.35:8070/test-toolkit/api/bmparam/generate/sit/LSSDF79SD7F97DS9F',
    ).text


provinces = '京津冀晋蒙辽吉黑沪苏浙皖闽赣鲁豫鄂湘粤桂琼渝川贵云藏陕甘青宁新'
cities_char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '1234567890ABCDEFGHKLMNPQRSTUVWXYZ'
city_index = 'ABCDGHJKLMNQSTWXYZ'


class CommonPage():
    def __init__(self, driver):
        self.driver = driver

    def wait(self):
        toast = self.driver.find_element_by_xpath("//div[@class='sq-toast-wrapper']")
        while toast.get_attribute('style') != 'display: none;':
            sleep(0.5)
            toast = self.driver.find_element_by_xpath("//div[@class='sq-toast-wrapper']")

    def page_down(self):
        chains = ActionChains(self.driver)
        chains.send_keys(Keys.PAGE_DOWN).perform()
        sleep(0.2)

    def click_btn(self, text):
        success = False
        while not success:
            try:
                self.driver.find_element_by_xpath(f"//button[div/span='{text}']").click()
                self.wait()
                success = True
            except WebDriverException:
                self.page_down()

    def click_item_span(self, label):
        self.driver.find_element_by_xpath(f"//li[div/div/span='{label}']//div[@class='list_right']/span").click()

    def click_item_button(self, label):
        self.driver.find_element_by_xpath(f"//li[div/div/span='{label}']//div[@class='offerBtn']").click()

    def check_agreement(self, txt):
        success = False
        while not success:
            try:
                self.driver.find_element_by_xpath(f"//span[contains(text(),'{txt}')]/..//i").click()
                self.wait()
                success = True
            except WebDriverException:
                self.page_down()



class FirstPage(CommonPage):
    def __init__(self, driver):
        self.driver = driver

    def close_float(self):
        self.driver.find_element_by_class_name('close-btn').click()

    def click_link(self, link):
        self.driver.find_element_by_xpath(f"//li[b='{link}']").click()

class SecondPage(CommonPage):
    def __init__(self, driver):
        self.driver = driver

    def default(self):
        self.choose_region('台湾省', '台北市')
        self.choose_dealer('台湾测试')
        self.set_license()
        self.click_btn('快捷报价')

    def choose_region(self, region, city):
        self.driver.find_element_by_xpath("//div[@class='sq-cell-head' and contains(text(),'投保城市')]").click()
        sleep(0.2)

        province_eles = self.driver.find_elements_by_xpath("//div[@class='sq-popup'][1]//div[@class='sq-picker-item'][1]//li")

        for i in range([item.text.strip() for item in province_eles].index(region) + 1):
            province_eles[i].click()
            sleep(0.2)

        city_eles = self.driver.find_elements_by_xpath("//div[@class='sq-popup'][1]//div[@class='sq-picker-item'][2]//li")

        for j in range([item.text.strip() for item in city_eles].index(city) + 1):
            city_eles[j].click()
            sleep(0.2)

        self.driver.find_element_by_xpath(f"//div[@class='sq-popup'][1]//div[text()='确认']").click()
        sleep(0.5)

    def choose_dealer(self, dealer):
        self.driver.find_element_by_xpath("//div[@class='sq-cell-head' and contains(text(),'经销商')]").click()
        sleep(0.2)
        dealer_eles = self.driver.find_elements_by_xpath("//div[@class='sq-popup'][2]//div[@class='sq-picker-item']//li")
        for i in range([item.text.strip() for item in dealer_eles].index(dealer) + 1):
            dealer_eles[i].click()
            sleep(0.2)
        self.driver.find_element_by_xpath(f"//div[@class='sq-popup'][2]//div[text()='确认']").click()
        sleep(0.2)

    def set_license(self, province='', city=''):
        sleep(0.5)
        self.driver.find_element_by_xpath("//span[@class='sq-carlicense-province']").click()
        sleep(0.5)
        self.driver.find_element_by_xpath(f"//li[text()='{random.choice(provinces)}']").click()
        sleep(0.5)
        self.driver.find_element_by_xpath(f"//li[text()='{random.choice(cities_char)}']").click()
        sleep(0.5)
        for _ in range(random.randint(5, 6)):
            sleep(0.2)
            self.driver.find_element_by_xpath(f"//li[text()='{random.choice(nums)}']").click()
        self.driver.find_element_by_xpath("//div[contains(text(),'车牌号')]").click()
        sleep(0.5)


class ThirdPage(CommonPage):
    def __init__(self, driver):
        self.driver = driver

    def click_label(self, label):
        self.driver.find_element_by_xpath(f"//div[@class ='sq-field' and div/span='{label}']").click()

    def choose_model(self, brand, model):
        self.click_label('品牌车型')
        sleep(1)
        self.driver.find_element_by_xpath(f"//div[@class='sq-brandCars']//li[div/span='{brand}']").click()
        sleep(1)
        self.driver.find_element_by_xpath(f"//div[@class='sq-selectcar']//li[contains(div, '{model}')]").click()
        sleep(1)
        self.driver.find_element_by_xpath("//ul[@class='sq-selectmodel-detail-ul']/li[1]").click()
        sleep(1)

    def set_input(self, label, value):
        self.driver.find_element_by_xpath(f"//div[div/span='{label}']//input").send_keys(value)

class ForthPage(CommonPage):
    def __init__(self, driver):
        self.driver = driver

class FifthPage(CommonPage):
    def __init__(self, driver):
        self.driver = driver



class SixthPage(CommonPage):
    def __init__(self, driver):
        self.driver = driver


def verify(url):
    mobile_emulation = {'deviceName': 'iPhone 6/7/8'}
    # mobile_emulation = {
    #     "deviceMetrics": {"width": 1920, "height": 1080, "pixelRatio": 3.0},
    #     "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) "
    #                  "AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
    # }
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', mobile_emulation)

    driver = webdriver.Chrome(executable_path='/Users/bida/Tool/selenium/chromedriver', options=options)
    driver.implicitly_wait(5)
    driver.get(url)

    first_page = FirstPage(driver)
    try:
        first_page.click_link('购买车险')
    except WebDriverException:
        first_page.close_float()
        first_page.click_link('购买车险')

    second_page = SecondPage(driver)
    second_page.default()

    third_page = ThirdPage(driver)
    third_page.choose_model('荣威', '荣威RX5')

    third_page.set_input('发动机号', 'FDS7FSD97FD')
    third_page.set_input('姓名', '张三')
    third_page.set_input('手机号', '13800138000')
    third_page.set_input('身份证号', '110101199901014791')
    third_page.click_btn('下一步')

    forth_page = ForthPage(driver)
    forth_page.click_item_button('太保财险')
    sleep(2)
    forth_page.click_item_span('太保财险')

    fifth_page = FifthPage(driver)
    fifth_page.click_btn('提交订单')

    sixth_page = SixthPage(driver)
    sixth_page.check_agreement('我已阅读')
    sixth_page.click_btn('投保并支付')

    print()

if __name__ == '__main__':
    url = get_url()
    verify(url)