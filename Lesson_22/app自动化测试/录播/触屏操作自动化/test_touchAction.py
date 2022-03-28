# -*- coding=utf-8 -*-
# @Time    : 2022/02/23 21:49
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.wait import WebDriverWait

"""
场景一【 需要登录或者特别的状态，就不适合每个都重启，启动一次就好】
    1、设置类setup_class,登录放在setup方法中；
    2、在teardown()发那个发中，每个用例都返回首页，self.driver.back()

    注意：和 desired_caps['noReset'] = 'true'，只是不清空app缓存情况下启动app；不能控制app启动次数，也不控制运行初始位置

场景二【打开app时，出现弹窗，需要用desired_caps['noReset'] = 'true'】
    1、只需要添加参数 desired_caps['noReset'] = 'true'
"""


@pytest.mark.skip
def test_start():
    os.system('adb shell am start -W -n com.xueqiu.android/.view.WelcomeActivityAlias -S')  # 打开app应用


class TestDw:
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
        desired_caps['noReset'] = 'true'  # 不清空app缓存，启动app（处理弹窗 ~ 点同意  ）

        # 首次启动时，不停止app（相当于debugging:在启动测试前的预停留页面开始测试）--> 设置为false后，取消debugger
        # desired_caps['dontStopAppOnReset'] = 'true'  # 设置为true后，就不执行driver.quit()
        desired_caps['skipDeviceInitialization'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # （全局）下面每个find都会等待
        self.driver.implicitly_wait(10)  # 存在于driver整个生命周期，全局（每个find均等待这个时间）

    @pytest.mark.skip
    def test_search_1(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        element_ = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        print(element_.text)
        print(element_.size)
        print(element_.location)
        if element_.is_displayed():
            element_.click()
            print("测试结束")
        else:
            print("测试失败")
        self.driver.back()

    @pytest.mark.skip
    def test_search_2(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        print(self.driver.find_element_by_id("com.xueqiu.android:id/tv_search"))
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        locator = (By.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']")
        # 方式1：【利用expected_conditions】WebDriverWait(self.driver, 10).until(ES.element_to_be_clickable(locator))
        # 方式2：【自定义函数】WebDriverWait类init方法中将self.driver转变为成员变量self._driver,until中的method调用成员变量self._driver
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element(*locator))  # 方法中一定要带一个参数x，因为until中会将self._driver传给该方法
        self.driver.find_element(*locator).click()

    @pytest.mark.skip
    def test_touchAction(self):
        if self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").is_enabled():
            touch_action_ = TouchAction(self.driver)  # 切记传入self,driver
            touch_action_.press(x=320, y=666).wait(300).move_to(x=320, y=300).release().perform()

    def test_window_rect(self):
        if self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").is_enabled():
            touch_action_ = TouchAction(self.driver)
            print(self.driver.get_window_rect())  # 打印屏幕尺寸（像素）
            win_rect = self.driver.get_window_rect()
            width = win_rect['width']
            height = win_rect['height']
            print(type(width))
            touch_action_.press(x=width/2, y=height*4/5).wait(300).move_to(x=width/2, y=height*1/5).release().perform()

    # 待优化
    def teardown(self):
        self.driver.quit()



