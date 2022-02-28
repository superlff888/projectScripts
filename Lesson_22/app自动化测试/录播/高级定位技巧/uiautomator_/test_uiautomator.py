# -*- coding=utf-8 -*-
# @Time    : 2022/02/24 23:09
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestUiAutomator:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1：7555'  # 自定义，随便命名
        desired_caps['appPackage'] = 'com.xueqiu.android'  # 每次执行setup，就会重新打开app
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'  # 每次执行setup，就会重新打开app
        # desired_caps['appActivity'] = '.common.MainActivity'  # 直接定义MainActivity，页面数据刷新有问题
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['ReSetKeyBoard'] = 'true'
        desired_caps['noReset'] = 'true'  # 不重置用户的操作状态（情况1：处理弹窗 ~ 点同意；情况2：之前登录过了  ）

        # 首次启动时，不停止app（相当于debugging:在启动测试前的预停留页面开始测试）--> 设置为false后，取消debugger
        # desired_caps['dontStopAppOnReset'] = 'true'  # 设置为true后，就不执行driver.quit()
        desired_caps['skipDeviceInitialization'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # （全局）下面每个find都会等待
        self.driver.implicitly_wait(10)  # 建议在setup中加隐式等待；存在于driver整个生命周期，全局（每个find均等待这个时间）

    @pytest.mark.skip
    def test_uiAutomator(self):
        pass

    def test_find_by_scroll(self):
        """滚动查找元素"""
        # 对首页的输入框做一个显示等待；返回self._driver.find_element(MobileBy.ID, element)
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search"))
        id_text = 'resourceId("com.xueqiu.android:id/title_text").text("推荐")'
        locator = (MobileBy.ANDROID_UIAUTOMATOR, id_text)
        # 判断“推荐”是否可点击
        WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()
        # print(list(self.driver.page_source))

        # 把想要查找的text文本输入text("")中
        locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                                 'scrollIntoView(new UiSelector().text("阿里巴巴").instance(0));')
        # WebDriverWait(self.driver, 3600).until(lambda x: x.find_element(*locator).text == "苹果")
        self.driver.find_element(*locator).click()

    def teardown(self):
        pass