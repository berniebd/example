# -*- encoding:utf-8 -*-
import random

from assertpy import assert_that
from bs4 import BeautifulSoup
from time import sleep

import cx_Oracle
import re
import pytest
import os
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
__auth__ = 'bida'

native_context = 'NATIVE_APP'
h5_context = 'WEBVIEW_com.tencent.mm:tools'
yingke_official_account = 'berniebd的接口测试号'

wechat_account = 'Tobot'
vehicle_owner = '饶博特'
phone = '18550016164'
vin1 = 'LSJA2222222222999'
vin2 = 'LSJA2222222222998'
party_nos = {'饶博特': 'C00000006183'}

desired_caps = {
    'platformName': 'Android',
    # 'deviceName': 'huawei-lld_a10',
    'deviceName': 'huawei-duk_al20',
    'platformVersion': '7.0',
    # 'platformVersion': '8.0',
    'fastReset': 'false',
    'appPackage': 'com.tencent.mm',
    'appActivity': '.ui.LauncherUI',
    'fullReset': 'False',
    'noReset': 'True',
    'unicodeKeyboard': 'False',
    'resetKeyboard': 'False',
    'chromeOptions': {
        # 'androidProcess': 'com.tencent.mm:appbrand0',
        'androidProcess': 'com.tencent.mm:tools',
    }
}


def find_element_by_xpath(driver, xpath):
    for _ in range(5):
        eles = driver.find_elements_by_xpath(xpath)
        if len(eles) > 0:
            return eles[0]
        sleep(1)
    raise Exception("no such element by xpath : {0}".format(xpath))


def find_elements_by_xpath(driver, xpath):
    for _ in range(5):
        eles = driver.find_elements_by_xpath(xpath)
        if len(eles) > 0:
            return eles
        sleep(1)
    return []


def untie_official_account(conn, account):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ECOWNER.EC_USER WHERE USER_CODE IN ("
                   "SELECT USER_CODE FROM ECOWNER.EC_BIND_USER WHERE APP_USER_NAME = '{0}')".format(account))
    cursor.execute("DELETE FROM ECOWNER.EC_USER_VEHICLE WHERE USER_CODE IN "
                   "(SELECT USER_CODE FROM ECOWNER.EC_BIND_USER WHERE APP_USER_NAME = '{0}')".format(account))
    cursor.execute("DELETE FROM ECOWNER.EC_BIND_USER WHERE APP_USER_NAME = '{0}'".format(account))
    cursor.close()
    conn.commit()


def update_customer_vehicle_ref(conn, vin, party_no=''):
    cursor = conn.cursor()
    cursor.execute("UPDATE CUSTOMEROWNER.CS_CUSTOMER_VEHICLE_REF SET PARTY_NO= '{0}' WHERE VEHICLE_NO IN "
                   "(SELECT VEHICLE_NO FROM CUSTOMEROWNER.CS_CUSTOMER_VEHICLE WHERE vin = '{1}' )"
                   .format(party_no, vin))
    cursor.close()
    conn.commit()


def enter_official_account(driver, account):
    # driver.find_element_by_android_uiautomator('new UiSelector().text("订阅号")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("通讯录")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("公众号")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("{}")'.format(account)).click()


def enter_yingke_personal_center(driver):
    if driver.current_context == h5_context:
        driver.switch_to.context(native_context)
        driver.find_element_by_id('com.tencent.mm:id/i2').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("个人中心")').click()
    driver.switch_to.context(h5_context)
    sleep(5)


def complete_account_info(conn, driver, name, phone):
    # find_element_by_xpath(driver, "//div[div/span='客户姓名']//input").send_keys(name)
    # find_element_by_xpath(driver, "//div[div/span='手机号码']//input").send_keys(phone)
    # clear_sms(conn, phone)
    # find_element_by_xpath(driver, "//button[contains(span, '获取验证码')]").click()
    # find_element_by_xpath(driver, "//input[@placeholder='请输入短信验证码']").send_keys(get_register_code(conn, phone))
    # find_element_by_xpath(driver, "//button[contains(span, '确认')]").click()

    driver.find_element_by_xpath("//div[div/span='客户姓名']//input").send_keys(name)
    driver.find_element_by_xpath("//div[div/span='手机号码']//input").send_keys(phone)
    clear_sms(conn, phone)
    driver.find_element_by_xpath("//button[contains(span, '获取验证码')]").click()
    driver.find_element_by_xpath("//input[@placeholder='请输入短信验证码']").send_keys(get_register_code(conn, phone))
    driver.find_element_by_xpath("//button[contains(span, '确认')]").click()


def tie_vehicle(driver, vin):
    # sleep(1)
    # find_element_by_xpath(driver, "//button[@class='add-car-btn']").click()
    # find_element_by_xpath(driver, "//div[contains(div/span,'车架号')]//input").send_keys(vin)
    # find_element_by_xpath(driver, "//div[contains(div/span,'行驶城市')]//input").click()
    # sleep(1)
    # find_element_by_xpath(driver, "//div[@class='van-picker__confirm']").click()
    # sleep(1)
    # find_element_by_xpath(driver, "//button[contains(span, '保存车辆')]").click()
    # sleep(5)

    sleep(1)
    driver.find_element_by_xpath("//button[@class='add-car-btn']").click()
    driver.find_element_by_xpath("//div[contains(div/span,'车架号')]//input").send_keys(vin)
    driver.find_element_by_xpath("//div[contains(div/span,'行驶城市')]//input").click()
    sleep(1)
    driver.find_element_by_xpath("//div[@class='van-picker__confirm']").click()
    sleep(1)
    driver.find_element_by_xpath("//button[contains(span, '保存车辆')]").click()
    sleep(5)

    


def untie_vehicle(driver, vin):
    # find_element_by_xpath(driver, "//div[contains(span, '{0}')]/../..//a[@class='remove-btn']".format(vin[-6:])).click()
    # find_element_by_xpath(driver, "//a[contains(text(), '确认')]").click()
    # sleep(5)
    driver.find_element_by_xpath("//div[contains(span, '{0}')]/../..//a[@class='remove-btn']".format(vin[-6:])).click()
    driver.find_element_by_xpath("//a[contains(text(), '确认')]").click()
    sleep(5)


def clear_sms(conn, phone):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ITBASEOWNER.SMS_SEND_LOG WHERE PHONE = '{}'".format(phone))
    cursor.close()
    conn.commit()


def get_register_code(conn, phone):
    cursor = conn.cursor()
    try:
        sleep(5)
        content = \
        cursor.execute("SELECT CONTENT FROM ITBASEOWNER.SMS_SEND_LOG WHERE PHONE='{}'".format(phone)).fetchall()[0][0]
        pattern = '您正在请求绑定手机，验证码为：(.*),3分钟内有效。请勿把验证码泄露给任何人。 回复TD退订'
        if re.search(pattern, content) is not None:
            register_code = re.search(pattern, content).groups()[0]
    except IndexError:
        raise Exception('验证短信发送失败')
    cursor.close()
    return register_code


def parse_html(page_source):
    return BeautifulSoup(page_source, 'html.parser')


class TestYingkePersonalCenter(object):
    pool = None
    conn = None
    driver = None

    def setup_class(self):
        self.pool = cx_Oracle.SessionPool(user='itbasedev', password='itbasedev', dsn='10.118.22.40:1521/sudbte',
                                          min=5, max=10, increment=1)
        self.conn = self.pool.acquire()

        self.driver = WebDriver('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
        self.driver.implicitly_wait(30)

    def teardown_class(self):
        self.pool.release(self.conn)
        # self.driver.quit()

    @pytest.mark.run(order=1)
    def test_complete_personal_info(self):
        # untie_official_account(conn, wechat_account)

        enter_official_account(self.driver, yingke_official_account)
        enter_yingke_personal_center(self.driver)
        sleep(5)

        # 用户关注后，需完善个人信息，才可执行操作
        # driver.find_element_by_xpath("//span[text()='我的卡券']").click()
        # assert_that('绑定').is_equal_to(parse_html(driver.page_source).title.text)
        #
        # driver.back()
        # driver.find_element_by_xpath("//span[text()='我的服务']").click()
        # assert_that('绑定').is_equal_to(parse_html(driver.page_source).title.text)
        #
        # driver.back()
        # driver.find_element_by_xpath("//button[contains(text(), '添加车辆信息')]").click()
        # assert_that('绑定').is_equal_to(parse_html(driver.page_source).title.text)

        # complete_account_info(conn, driver, vehicle_owner, phone)

        # 完善个人信息后，主动绑定车辆，并关联卡券、服务
        # driver.find_element_by_xpath("//span[text()='我的卡券']").click()
        # sleep(5)
        # assert_that(len(driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin1)))).is_equal_to(1)
        # assert_that(len(driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin2)))).is_equal_to(1)
        #
        # driver.back()
        # driver.find_element_by_xpath("//span[text()='我的服务']").click()
        # sleep(5)
        # assert_that(len(driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin1)))).is_equal_to(0)
        # assert_that(len(driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin2)))).is_equal_to(1)


    # 添加车辆，同时绑定卡券、服务
    @pytest.mark.run(order=3)
    def test_tie_vehicle(self):
        enter_yingke_personal_center(self.driver)
        self.driver.find_element_by_xpath("//button[contains(text(), '车辆管理')]").click()
        sleep(2)
        tie_vehicle(self.driver, vin2)
        assert_that(len(self.driver.find_elements_by_xpath("//div[@class='wrapper']"))).is_equal_to(2)

        enter_yingke_personal_center(self.driver)
        self.driver.find_element_by_xpath("//span[text()='我的卡券']").click()
        sleep(5)
        assert_that(len(self.driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin2)))).is_equal_to(1)

        enter_yingke_personal_center(self.driver)
        self.driver.find_element_by_xpath("//span[text()='我的服务']").click()
        assert_that(len(self.driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin2)))).is_equal_to(1)


    # 删除车辆，卡券、服务同时解绑
    @pytest.mark.run(order=2)
    def test_untie_vehicle(self):
        enter_yingke_personal_center(self.driver)
        self.driver.find_element_by_xpath("//button[contains(text(), '车辆管理')]").click()
        sleep(2)
        untie_vehicle(self.driver, vin2)
        assert_that(len(self.driver.find_elements_by_xpath("//div[@class='wrapper']"))).is_equal_to(1)
        enter_yingke_personal_center(self.driver)
        self.driver.find_element_by_xpath("//span[text()='我的卡券']").click()
        assert_that(len(self.driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin2)))).is_equal_to(0)

        enter_yingke_personal_center(self.driver)
        self.driver.find_element_by_xpath("//span[text()='我的服务']").click()
        assert_that(len(self.driver.find_elements_by_xpath("//span[contains(text(), '{0}')]".format(vin2)))).is_equal_to(0)

# def ran():
#     e = ''
#     for _ in range(5):
#         ran = random.randint(1, 6)
#         if ran == 2:
#             return ran
#         else:
#             e = e + str(ran)
#             e = e + ','
#     raise Exception('not randomed: {}'.format(e))
#
# if __name__ == '__main__':
#     print(ran())