# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:14
# @Author  : ╰☆H.俠ゞ
# =============================================================


import logging
import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

from Lesson_22.web_autoTest.PageObject_battle_web.page_object.add_member_page import AddMemberPage
from Lesson_22.web_autoTest.PageObject_battle_web.page_object.contact_page import ContactPage
from Lesson_22.web_autoTest.PageObject_battle_web.page_object.login import Login

"""
首页
"""


class MainPageObject(Login):
    # 可以写在配置文件中，去读取
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#index"  # 类属性重写，重写了_BASE_URL

    # 跳转到“通讯录”页面的功能
    def goto_contact_page(self):
        return ContactPage()

    # 跳转到“添加成员”页面的功能
    def goto_add_member_page(self):
        # 点击添加成员按钮
        self.fond(By.CSS_SELECTOR, ".ww_indexImg_AddMember").click()  # c继承b，b继承a，则c也继承a的方法
        return AddMemberPage(self.driver)  # WebDriver Object赋值于新页面的driver