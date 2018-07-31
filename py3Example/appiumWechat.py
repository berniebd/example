# -*- encoding:utf-8 -*-
from time import sleep

from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver import DesiredCapabilities

__auth__ = 'bida'

def wechat_retur(driver):
    driver.switch_to.context('NATIVE_APP')
    # eles = driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/js")')
    driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.tencent.mm:id/js")').click()
    driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')


if __name__ == '__main__':
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
            'androidProcess': 'com.tencent.mm:appbrand0'
        }
    }

    driver = WebDriver('http://localhost:4723/wd/hub', desired_capabilities=desired_caps)
    driver.implicitly_wait(30)
    driver.find_element_by_android_uiautomator('new UiSelector().text("发现")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("小程序")').click()
    driver.find_element_by_android_uiautomator('new UiSelector().text("京东购物")').click()
    # driver.find_element_by_android_uiautomator('new UiSelector().text("宜家会员活动")').click()
    print(driver.contexts)
    driver.switch_to.context('WEBVIEW_com.tencent.mm:appbrand0')

    main_handler = ''
    for _ in range(10):
        handles = driver.window_handles
        find = False
        for handler in handles:
            driver.switch_to.window(handler)
            if driver.find_elements_by_xpath("//wx-view[text()='定制频道']"):
                main_handler = handler
                driver.find_element_by_xpath("//wx-view[text()='定制频道']").click()
                find = True
                break
        if find:
            break
        else:
            sleep(1)

    channel_handler = ''
    for _ in range(10):
        handles = driver.window_handles
        find = False
        for handler in handles:
            driver.switch_to.window(handler)
            if driver.find_elements_by_xpath("//wx-view[text()='保存']"):
                channel_handler = handler
                # driver.find_element_by_xpath("//wx-view[text()='保存']").click()
                find = True
                break
        if find:
            break
        else:
            sleep(1)

    wechat_retur(driver)

    coupon_handler = ''
    for _ in range(10):
        handles = driver.window_handles
        find = False
        for handler in handles:
            driver.switch_to.window(handler)
            if driver.find_elements_by_xpath("//wx-view[text()='领优惠券']"):
                coupon_handler = handler
                driver.find_element_by_xpath("//wx-view[text()='领优惠券']").click()
                find = True
                break
        if find:
            break
        else:
            sleep(1)


