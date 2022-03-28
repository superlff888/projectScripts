# -*- coding=utf-8 -*-
# @Time    : 2022/02/28 23:18
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class Test_contact:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '11.0'
        desired_caps['deviceName'] = 'emulator-5554'  # 自定义，随便命名
        desired_caps['appPackage'] = 'com.tencent.wework'  # 每次执行setup，就会重新打开app
        desired_caps['appActivity'] = '.launch.LaunchSplashActivity'  # app的第一个activity
        desired_caps['unicodeKeyboard'] = 'true'
        desired_caps['ReSetKeyboard'] = 'true'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)  # 建议在setup中加隐式等待；存在于driver整个生命周期，全局（每个find均等待这个时间）

    def teardown(self):
        self.driver.quit()

    def test_mobile(self):
        # self.driver.send_sms('15715151010', 'Hey Boy')
        # self.driver.make_gsm_call('15715151010', GsmCallActions.CALL)
        self.driver.start_recording_screen()  # 开始录屏 （android 8.0以上）
        self.driver.get_screenshot_as_file(os.getcwd() + r"\photos\img.png")
        print(os.getcwd())
        self.driver.stop_recording_screen()  # 结束录屏
