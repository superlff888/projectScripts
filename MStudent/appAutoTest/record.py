# -*- coding=utf-8 -*-
# @Time    : 2023/02/26 14:44
# @Author  : ╰☆H.俠ゞ
# =============================================================
import subprocess

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import TouchActions


class Test_max:

    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = '127.0.0.1:7555'  # 自定义，随便命名
        desired_caps['udid'] = '127.0.0.1:7555'  # 多个设备时，指定要使用的设备
        desired_caps['AutoGrantPermissions'] = True  # 自动授予系统信息权限等（不用手动做同意操作）注意：noReset 设置为'true'后,此参数失效
        desired_caps['appPackage'] = 'com.tencent.wework'  # 每次执行setup，就会重新打开app
        desired_caps['appActivity'] = '.launch.WwMainActivity'  # app的第一个activity
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['ReSetKeyBoard'] = 'true'
        desired_caps['skipServerInstallation'] = 'true'  # 跳过 uiautomator2 server的安装 （手机端 appium setting）
        desired_caps['skipDeviceInitialization'] = 'true'  # 跳过设备初始化
        desired_caps['noReset'] = 'true'  # 记录用户操作session；不重置用户的操作状态（情况1：处理弹窗 ~ 点同意；情况2：之前登录过了  ）
        desired_caps['newCommandTimeout'] = 300  # 超时时间
        desired_caps['settings[waitForIdleTimeout]'] = 0  # 等待页面完全加载完成的时间
        '''# 首次启动时，不停止app（相当于debugging:在启动测试前的预停留页面开始测试）--> 设置为false后，取消debugger'''
        # desired_caps['dontStopAppOnReset'] = 'true'  # 设置为true后，就不执行driver.quit()
        desired_caps['skipDeviceInitialization'] = 'true'
        # 最重要的一句，与远程服务建立连接，返回一个 session 对象
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        # 在调用find_element() 的时候,会每隔0.5秒查找一次元素（全局）；driver即是session（注意session的有效期）
        self.driver.implicitly_wait(10)  # 建议在setup中加隐式等待；存在于driver整个生命周期，全局（每个find均等待这个时间）


caps = {}
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", ca
driver.find_element(MobileBy.ACCESSIBILITY_ID, "同意")

# 方法返回的是字典
driver.press_keycode(KEYCODE_HOME)