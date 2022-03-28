# -*- coding=utf-8 -*-
# @Time    : 2022/02/27 14:51
# @Author  : ╰☆H.俠ゞ
# =============================================================
import datetime
import logging
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from Lesson_22.app自动化测试.myBattle_app.location.swipe_find import swipe_fond


class Test_contact:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'  # 自定义，随便命名
        desired_caps['udid'] = '127.0.0.1:7555'  # 多个设备时，指定要使用的设备
        desired_caps['AutoGrantPermissions'] = 'True'  # 自动授予系统信息权限等（不用手动做同意操作）注意：noReset 设置为'true'后,此参数失效
        desired_caps['appPackage'] = 'com.tencent.wework'  # 每次执行setup，就会重新打开app
        desired_caps['appActivity'] = '.launch.WwMainActivity'  # app的第一个activity
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['ReSetKeyBoard'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装，提高启动速度
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化（手机端 appium setting），提高运行速度
        desired_caps['noReset'] = 'true'  # 记录用户操作session；不重置用户的操作状态（情况1：处理弹窗 ~ 点同意；情况2：之前登录过了  ）
        # desired_caps['newCommandTimeout'] = 300  # 超时时间
        # 等待页面完全加载完成的时间
        desired_caps['settings[waitForIdleTimeout]'] = 0  # (也可在方法中update_settings({"waitForIdleTimeout": 0}))
        '''# 首次启动时，不停止app（相当于debugging:在启动测试前的预停留页面开始测试）--> 设置为false后，取消debugger'''
        # desired_caps['dontStopAppOnReset'] = 'true'  # 设置为true后，就不执行driver.quit()
        # 最重要的一句，与远程服务建立连接，返回一个 session 对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 在调用find_element() 的时候,会每隔0.5秒查找一次元素（全局）；driver即是session（注意session的有效期）
        self.driver.implicitly_wait(10)  # 建议在setup中加隐式等待；存在于driver整个生命周期，全局（每个find均等待这个时间）

    def teardown(self):
        self.driver.quit()

    def test_contact(self):
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='通讯录']"))
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'添加成员')]").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()
        # 输入姓名  text属性值包含“姓名”
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '姓名')]/../android.widget.EditText").send_keys('lee')
        # 输入手机号
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'手机')]/..//*[contains(@text,'必填')]").send_keys(15715151010)
        # 点击保存
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text, '保存')]").click()
        # 手机已存在
        self.driver.find_element(MobileBy.XPATH, "//*[@text='确定']").click()

    def swipe_fond(self, text, num=3):  #
        """
        滑动查找目标元素的text
        根据滑动的距离，可预置滑动的次数
        滑动时间为2000ms
        Up and down
        """
        for i in range(num):
            try:
                element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
                logging.debug(f"已经找到目标元素对应的text：{text}")
                return element
            except Exception as e:
                print("未找到")
                logging.debug(f"debug:{e}")
                size = self.driver.get_window_size()  # 获取当前屏幕的尺寸（不同设备，坐标不同，可能无法滑动）
                # 'width', 'height'
                width = size.get("width")
                height = size.get("height")
                start_x = width / 2
                start_y = height * 0.8
                end_x = start_x
                end_y = height * 0.3
                self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
            if i == num - 1:
                raise NoSuchElementException(f"找了{num}次，未找到元素")  # 次数用完，抛异常NoSuchElement

    def test_workbench(self):
        WebDriverWait(self.driver, 20).until(lambda x: x.find_element(MobileBy.XPATH, "//*[@text='工作台']"))
        self.driver.find_element(MobileBy.XPATH, "//*[@text='工作台']").click()
        self.swipe_fond("打卡", 5).click()
        self.driver.update_settings({"waitForIdleTimeout": 0})  # 待页面完全加载完成的时间
        print(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S'))
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[contains(@text,'次外出')]").click()
        print(datetime.datetime.now().strftime('%Y%m%d %H:%M:%S'))
        WebDriverWait(self.driver, 20).until(lambda x: '外出打卡成功' in x.page_source)
        # 验证（自带断言，找不到元素就返回NoSuchElement）
        self.driver.find_element(MobileBy.XPATH, "//*[@text='外出打卡成功']")
        self.driver.page_source()
