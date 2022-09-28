# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:14
# @Author  : ╰☆H.俠ゞ
# =============================================================


import time

import yaml

from Lesson_22.web_autoTest.PageObject_battle_web.page_object.base_page import BasePage


class Login(BasePage):
    """
    是企业微信的公共业务的封装
    """
    # base_url是指每个页面的url
    _BASE_URL = ""  # _ 私有属性可以被重写，肯定是可以被继承的，但是子类无法访问父类的保护属性;  __私有属性更不能访问;
    """如果将self.driver.get(self._BASE_URL)封装在基类中，则"""
    def login(self):
        # 打开index 页面
        self.driver.get(self._BASE_URL)
        cookie = yaml.safe_load(open("../data/cookie.yaml"))
        # 3. 植入cookie
        for c in cookie:
            self.driver.add_cookie(c)
        time.sleep(3)
        # 4.再次访问企业微信页面，发现无需扫码自动登录，而且可以多次使用
        self.driver.get(self._BASE_URL)

    def back_start_page(self):
        """
        回退到用例开始的页面。
        :return:
        """
        self.driver.get(self._BASE_URL)