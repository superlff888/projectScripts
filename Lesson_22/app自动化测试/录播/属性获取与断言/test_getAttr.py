# -*- coding=utf-8 -*-
# @Time    : 2022/02/26 20:16
# @Author  : ╰☆H.俠ゞ
# =============================================================
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestGetAttr:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1：7555'  # 自定义，随便命名
        desired_caps['appPackage'] = 'com.xueqiu.android'  # 每次执行setup，就会重新打开app
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'  # 每次执行setup，就会重新打开app
        # desired_caps['appActivity'] = '.commonWework.MainActivity'  # 直接定义MainActivity，页面数据刷新有问题
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['ReSetKeyBoard'] = 'true'
        desired_caps['noReset'] = 'true'  # 不重置用户的操作状态（情况1：处理弹窗 ~ 点同意；情况2：之前登录过了  ）

        # 首次启动时，不停止app（相当于debugging:在启动测试前的预停留页面开始测试）--> 设置为false后，取消debugger
        desired_caps['dontStopAppOnReset'] = True  # 设置为true后，就不执行driver.quit()
        desired_caps['skipDeviceInitialization'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # （全局）下面每个find都会等待
        self.driver.implicitly_wait(10)  # 建议在setup中加隐式等待；存在于driver整个生命周期，全局（每个find均等待这个时间）

    def test_getAttr(self):
        search_element = self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search")
        print(f"\n{search_element.get_attribute('bounds')}")
        print(search_element.get_attribute('resource-id'))
        print(search_element.get_attribute('clickable'))

    def teardown(self):
        pass

