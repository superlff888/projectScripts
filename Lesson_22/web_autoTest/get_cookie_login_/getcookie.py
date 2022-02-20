# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 21:59
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""
【思路】
1、打开浏览器，扫码登录
2、【重点！！！！！！】 确保登录后（重点！！！），再通过get_cookies获得cookie
3、检查本地文件是否获取成功
4、再次打开浏览器，通过z植入cookie直接进入目标主页!

"""


# 获取cookies  driver.get_cookies()
import os
from time import sleep

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait


class TestCookieLogin:
    def setup_class(self):
        self.driver = webdriver.Chrome()

    #  通过get_cookies获得cookie_list
    def test_get_cookies(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 扫码登录,显示等待企业微信登录成功
        WebDriverWait(self.driver, 20).until(e.visibility_of_element_located((By.CSS_SELECTOR, '.index_explore_title')))
        # 企业微信登录成功后，获得cookie
        cookie_list = self.driver.get_cookies()
        print(cookie_list)
        # 将cookie存储于一个可持久化的地方（数据库或文件）
        with open(os.path.dirname(__file__) + "/cookie.yml", "w") as file:  # 获取当前文件的根目录，再做字符串拼接
            # 参数1：要写入的数据(Python对象); 参数2：要存放的文件流(这里放在了打开的文件中)
            yaml.safe_dump(cookie_list, file)  # 将 Python 对象序列化为 YAML流(文件)。 Python 对象，如 str、dict、set、list

    # 植入cookie  driver.add_cookie(cookie)
    def test_add_cookie_login(self):
        # 访问企业微信主页
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")
        # 从已经写入的cookie.yml文件中获取
        cookie = yaml.safe_load(open(os.path.dirname(__file__) + "./cookie.yml"))
        # cookie = yaml.safe_load(open(r"D:\Develop\git_pub_repositories\projectScripts\Lesson_22\web_autoTest\get_cookie_login_\cookie.yml"))
        # 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        sleep(2)
        # 再次访问企业微信，发现无需扫码，自动登录
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")