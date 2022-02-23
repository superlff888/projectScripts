# -*- coding=utf-8 -*-
# @Time    : 2022/02/23 21:49
# @Author  : ╰☆H.俠ゞ
# =============================================================

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TestDw:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1：7555'  # 自定义，随便命名
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = '.common.MainActivity'
        desired_caps['noReSet'] = 'true'  # 处理弹窗（点同意） ~ 记住之前的动作，住操作缓存信息
        # desired_caps['dontStopAppOnReSet'] = 'true'  # 首次启动时，不停止app（相当于debugging）--> 注释掉或设置为false后，重新启动app
        desired_caps['skipDeviceInitialization'] = 'true'  # 首次启动时，不停止app（相当于web自动化的debugger；注意保证该页面元素能够定位到）
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 下面每一步都会等待
        self.driver.implicitly_wait(10)  # 存在于driver整个生命周期，全局（每个find军等待这个时间）

    def test_search(self):
        # TouchAction(driver).tap(x=105, y=473).perform()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("alibaba")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]/android.widget.LinearLayout/android.widget.TextView[1]")
        el4.click()

        TouchAction(self.driver).tap(x=105, y=473).perform()
        el2 = self.driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el2.click()
        el3 = self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el3.send_keys("alibaba")
        el4 = self.driver.find_element_by_xpath(
            "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[7]/android.widget.LinearLayout/android.widget.TextView[1]")
        el4.click()

    def teardown(self):
        self.driver.quit()



