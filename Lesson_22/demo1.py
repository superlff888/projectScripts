# -*- coding=utf-8 -*-
# @Time    : 2022/02/24 01:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
from appium import webdriver

desired_caps = {
    "platformName": "Android",
    "deviceName": "127.0.0.1:7555",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "noReset": "true",
    "dontStopAppOnReset": "true",
    "skipDeviceInitialization": "true"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)
el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
driver.quit()