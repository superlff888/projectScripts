# -*- coding=utf-8 -*-
# @Time    : 2022/02/21 23:06
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
遇到报错，还一个工程试试！！！
原因：可能是因为虚拟环境的原因
"""
from time import sleep

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = '127.0.0.1：7555'  # 自定义，随便命名
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.common.MainActivity'
desired_caps['noReSet'] = 'true'  # 处理弹窗（点同意） ~ 记住之前的动作，住操作缓存信息
desired_caps['dontStopAppOnReSet'] = 'true'  # 首次启动时，不停止app（相当于debugging）


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
el1.click()
driver.implicitly_wait(3)  # 存在于driver整个生命周期，全局（每个find军等待这个时间）
el2 = driver.find_element_by_id("com.xueqiu.android:id/action_close")
el2.click()
driver.back()
sleep(3)  # 强等待
