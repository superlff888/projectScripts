# -*- coding=utf-8 -*-
# @Time    : 2022/02/21 23:06
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
遇到报错，还一个工程试试！！！可能文件夹中文太多了
"""

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-5554'  # 自定义，随便命名
# com.android.settings/com.android.settings.Settings
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.android.settings.Settings'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
driver.implicitly_wait(3)
el2 = driver.find_element_by_id("com.xueqiu.android:id/action_close")
el2.click()
driver.implicitly_wait(3)
driver.back()
driver.implicitly_wait(3)
