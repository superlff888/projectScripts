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
        desired_caps['appActivity'] = 'com.xueqiu.android.view.WelcomeActivityAlias'  # 需要初始的activiity
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['ReSetKeyBoard'] = 'true'
        desired_caps['noReSet'] = 'true'  # 测试前后是否重置环境 【处理弹窗（点同意） ~ 记住之前的动作，操作缓存信息】
        desired_caps['dontStopAppOnReSet'] = 'true'  # 首次启动时，不停止app（相当于debugging:停留在那个页面，就从那个页面开始执行测试）
        desired_caps['skipDeviceInitialization'] = 'true'  # 不清理（不执行driver.quit()）
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 下面每一步都会等待
        self.driver.implicitly_wait(10)  # 存在于driver整个生命周期，全局（每个find军等待这个时间）

    @pytest.mark.skip
    def test_search_1(self):
        self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
        self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
        sleep(3)
        self.driver.find_element_by_id("com.xueqiu.android:id/name").click()

    def test_attr(self):
        element = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        ele_enable = element.is_enabled()  # 判断是否可用
        print(element.text)  # 元素内的超文本内容
        print(element.location)  # 元素左上角坐标
        print(element.size)  # 宽和高
        if ele_enable:
            element.click()
            self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
            ele_alibaba = self.driver.find_element_by_xpath("//*[@resource-id = 'com.xueqiu.android:id/name' and @text = '阿里巴巴']")
            # ele_alibaba.is_displayed()  # 方法一：判断是否可见
            ele_displayed = ele_alibaba.get_attribute("displayed")  # 获取属性"displayed"的值，true为可见
            print(ele_displayed)  # 返回的true是str （不是布尔类型值 True）
            if ele_displayed == 'true':
                ele_alibaba.click()
                print("搜索成功")
            else:
                print("搜索失败")
        touch = TouchAction(self.driver)
        # 按下并由A移动到B，然后释放; 必须执行perform
        touch.press(x=320, y=666).wait(200).move_to(x=320, y=310).release().perform()  # 等待200毫秒
        print("向下滑动")

    # @pytest.mark.skip
    def test_touchAction(self):  # 一般不用坐标轴
        print("执行了")
        if self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").is_displayed():
            touch = TouchAction(self.driver)
            # 按下并由A移动到B，然后释放; 必须执行perform;等待200毫秒; 点的坐标由A移动到B
            touch.press(x=328, y=666).wait(200).move_to(x=328, y=328).release().perform()
            sleep(3)

    def teardown(self):
        self.driver.quit()
