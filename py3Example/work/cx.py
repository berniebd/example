# -*- coding: utf-8 -*-
# Created by bida on 2018/9/12
import random

from selenium.common.exceptions import WebDriverException, NoSuchElementException
from time import sleep

import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


def get_url():
    return requests.post(
        url='http://10.118.22.35:8070/test-toolkit/api/cxparam/v2/generate',
        json={"env": "sit", "province": "320000", "city": "320400", "userId": "YVRDjD0zbOHVeznN3EF1jg"}
    ).text


provinces = '京津冀晋蒙辽吉黑沪苏浙皖闽赣鲁豫鄂湘粤桂琼渝川贵云藏陕甘青宁新'
cities = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nums = '1234567890ABCDEFGHKLMNPQRSTUVWXYZ'
city_index = 'ABCDGHJKLMNQSTWXYZ'


class CommonPage():
    def __init__(self, driver):
        self.driver = driver
        self.wait()

    def wait(self):
        while 1:
            try:
                ele = self.driver.find_element_by_xpath("//div[@class='sq-toast-wrapper']")
                if ele.is_displayed():
                    sleep(1)
                    continue
                else:
                    break
            except WebDriverException:
                break

    def set_value(self, label, value):
        ele = self.driver.find_element_by_xpath("//li[div='{0}']/input".format(label))
        for _ in range(6):
            try:
                ele.send_keys(value)
                break
            except WebDriverException:
                sleep(1)
                continue

    def click(self, ele):
        for _ in range(6):
            try:
                ele.click()
                break
            except WebDriverException:
                sleep(1)
                continue

    def submit(self, text):
        self.driver.find_element_by_xpath(f"//button[//span='{text}']").click()
        self.wait()

    def get_swtich(self, label):
        return self.driver.find_element_by_xpath(f"//li[div='{label}']/div[@class='switch']/div")

    def switch(self, label):
        self.get_swtich(label).click()

    def check_agreement(self, txt):
        self.driver.find_element_by_xpath(f"//span[contains(text(),'{txt}')]/..//i").click()

    def page_down(self):
        chains = ActionChains(self.driver)
        chains.send_keys(Keys.PAGE_DOWN).perform()
        sleep(0.2)


class FirstPage(CommonPage):
    def __init__(self, driver):
        self.driver = driver

    def default(self):
        self.set_license()
        self.driver.find_element_by_xpath("//div[div/span='推荐码']//input").send_keys('berniee')
        self.driver.find_element_by_xpath("//button[div/span='查询报价']").click()

    def set_license(self, province='', city=''):
        sleep(0.1)
        self.driver.find_element_by_xpath("//span[@class='sq-carlicense-province']").click()
        sleep(0.5)
        self.driver.find_element_by_xpath("//li[text()='京']").click()
        sleep(0.5)
        self.driver.find_element_by_xpath("//li[text()='B']").click()
        sleep(0.5)
        for _ in range(random.randint(5, 6)):
            sleep(0.1)
            index = random.randint(0, 32)
            print(index)
            self.driver.find_element_by_xpath("//li[text()='{0}']".format(nums[index])).click()

        self.driver.find_element_by_xpath("//div[@class='sq-carlicense']//a[@class='sq-carlicense-close-btn-text']").click()


class SecondPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def default(self):
        self.set_value('车辆识别码', 'lsjs0000000000084')
        self.set_value('发动机号', '000083')

        ele3 = self.driver.find_element_by_xpath("//li[div='注册日期']")
        self.click(ele3)
        sleep(1)

        default_year, default_month, default_day = 2018, 10, 18
        default_year_index, default_month_index, default_day_index = -1, 9, 17
        year, month, day = 2016, 11, 24

        li_year = self.driver.find_elements_by_xpath("(//div[@class='sq-popup'][1]//ul)[1]//li")
        for i in range(abs(year - default_year)):
            if year > default_year:
                li_year[default_year_index + 1 + i].click()
            if year < default_year:
                li_year[default_year_index - 1 - i].click()
            sleep(0.1)

        li_month = self.driver.find_elements_by_xpath("(//div[@class='sq-popup'][1]//ul)[2]//li")
        for i in range(abs(month - default_month)):
            if month > default_month:
                li_month[default_month_index + 1 + i].click()
            if month < default_month:
                li_month[default_month_index - 1 - i].click()
            sleep(0.1)

        li_day = self.driver.find_elements_by_xpath("(//div[@class='sq-popup'][1]//ul)[3]//li")
        for i in range(abs(day - default_day)):
            if day > default_day:
                li_day[default_day_index + 1 + i].click()
            if day < default_day:
                li_day[default_day_index - 1 - i].click()
            sleep(0.1)

        ele6 = self.driver.find_element_by_xpath("(//div[@class='sq-popup'])[1]//div[text()='确认']")
        self.click(ele6)
        self.set_value('姓名', '伯尼')
        self.set_value('手机号', '18600365141')
        self.set_value('身份证号', '110101199901014791')
        # self.set_value('民族', '汉')
        # self.set_value('地址', '北京市大望路')

        sleep(2)
        self.driver.find_element_by_xpath("//span[@class='sq-checkicon-wrap']").click()
        self.driver.find_element_by_xpath("//button[//span='我要报价']").click()


class ThirdPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_vehicle_model(self, model):
        self.driver.find_element_by_xpath("//li[div='品牌车型']").click()
        self.driver.find_element_by_xpath("//div[@class='sq-brandCars']//ul/li[1]/input").send_keys(model)
        self.driver.find_element_by_xpath("//div[@class='sq-brandCars']//ul/li[1]/i").click()
        self.driver.find_element_by_xpath("//div[@class='sq-search']//ul/li[1]").click()

    def default(self):
        self.set_vehicle_model('svw73010vk')
        self.switch('交强险')
        sleep(2)
        self.submit('我要报价')


class ForthPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_quote_result(self, insurer):
        try:
            return self.driver.find_element_by_xpath(
                f"//ul[@class='offerList']//span[text()='{insurer}']/../..//div[@class='list-right']/span").text()
        except NoSuchElementException:
            return ''

    def quote(self, insurer):
        self.driver.find_element_by_xpath(
            f"//ul[@class='offerList']//span[text()='{insurer}']/../..//div[@class='offerBtn']").click()
        self.wait()

    def detail(self, insurer):
        self.driver.find_element_by_xpath(
            f"//ul[@class='offerList']//span[text()='{insurer}']/../..//div[@class='list_right']/span").click()
        self.wait()


class FifthPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def adjust(self):
        self.driver.find_element_by_xpath("//a[text()='调整方案']").click()


class SixthPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def check_clause(self, clause):
        pass

    def uncheck_clause(self, clause):
        pass

    def get_special_clause_icon(self, clause):
        return self.driver.find_element_by_xpath(f"//div[div='{clause}']/span/i")

    def check_special_clause(self, clause):
        self.get_special_clause_icon(clause).click()

class SeventhPage(CommonPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def set_delivery_address(self):
        self.page_down()
        self.driver.find_element_by_xpath("//div[text()='添加配送地址']").click()
        self.set_value('收件人', '张三')
        self.set_value('手机号', '13800138000')
        self.driver.find_element_by_xpath("//div[span='选择地区']").click()
        sleep(0.2)
        self.driver.find_element_by_xpath("//div[@class='sq-popup']//div[text()='确认']").click()
        sleep(0.1)
        self.set_value('街道地址', '海淀区大柳树')
        sleep(0.1)
        self.driver.find_element_by_xpath("//div[@class='saveBtn']").click()


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
    sleep(2)

    first_page = FirstPage(driver)
    first_page.default()
    second_page = SecondPage(driver)
    second_page.default()
    third_page = ThirdPage(driver)
    third_page.default()

    forth_page = ForthPage(driver)
    forth_page.quote('平安财险')
    forth_page.detail('平安财险')
    fifth_page = FifthPage(driver)
    fifth_page.adjust()

    sixth_page = SixthPage(driver)
    sixth_page.check_special_clause('机动车损失险')
    sixth_page.submit('保存')

    fifth_page.submit('提交订单')

    seventh_page = SeventhPage(driver)
    seventh_page.set_delivery_address()
    # sleep(2)
    chains = ActionChains(driver)

    chains.send_keys(Keys.PAGE_DOWN).perform()

    success = False
    while not success:
        try:
            seventh_page.check_agreement('我已阅读')
            success = True
        except WebDriverException:
            chains.send_keys(Keys.PAGE_DOWN).perform()

    seventh_page.submit('投保并支付')

    # driver.close()


if __name__ == '__main__':
    verify(get_url())
