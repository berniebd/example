#encoding=utf-8
__author__ = 'bida'

from appium import webdriver

if __name__ == '__main__':
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.0.1'
    desired_caps['deviceName'] = 'huawei-plk_ul00-W8R0215813002079'
    desired_caps['app'] = 'e:/example.apk'
    desired_caps['unicodekeyboard'] = 'True'
    desired_caps['resetKeyboard'] = 'True'

    # print dir(webdriver)
    client = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    client.implicitly_wait(15)

    client.find_element_by_android_uiautomator('new UiSelector().resourceId("com.wandoujia.phoenix2:id/search_image")').click()

    client.back()

    client.find_element_by_android_uiautomator('new UiSelector().resourceId("com.wandoujia.phoenix2:id/search_box_close")').click()

    client.find_element_by_android_uiautomator('new UiSelector().resourceId("com.wandoujia.phoenix2:id/search_box_edit")')\
        .send_keys('腾讯')