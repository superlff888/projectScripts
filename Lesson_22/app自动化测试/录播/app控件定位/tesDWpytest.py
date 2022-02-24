# -*- coding=utf-8 -*-
# @Time    : 2022/02/23 21:49
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDw:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1：7555'  # 自定义，随便命名
        desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = '.common.MainActivity'  # 直接定义MainActivity，页面数据刷新有问题
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['ReSetKeyBoard'] = 'true'
        desired_caps['noReset'] = 'true'  # 处理弹窗（点同意） ~ 记住之前的动作，住操作缓存信息
        desired_caps['dontStopAppOnReset'] = 'true'  # 首次启动时，不停止app（相当于debugging）--> 注释掉或设置为false后，重新启动app
        desired_caps['skipDeviceInitialization'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # （全局）下面每个find都会等待
        self.driver.implicitly_wait(10)  # 存在于driver整个生命周期，全局（每个find军等待这个时间）

    def test_search_1(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()

    # def teardown(self):
    #     self.driver.quit()



