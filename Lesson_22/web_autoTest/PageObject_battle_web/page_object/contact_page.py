# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:13
# @Author  : ╰☆H.俠ゞ
# =============================================================


import time

from selenium.webdriver.common.by import By

from Lesson_22.web_autoTest.PageObject_battle_web.page_object.base_page import BasePage


from Lesson_22.web_autoTest.PageObject_battle_web.page_object.login import Login

"""
通讯录界面
"""


class ContactPage(Login):
    _BASE_URL = "https://work.weixin.qq.com/wework_admin/frame#contacts"  # 重写父类属性

    # 跳转到“添加成员的页面”
    def goto_add_member(self):
        pass

    # 获取成员列表（仅取姓名）
    def get_member_list(self):
        """
        获取成员列表
        :return:
        """
        # 利用css，获得列表中每行的第二个元素
        ele_list = self.driver.find_elements(By.CSS_SELECTOR, ".member_colRight_memberTable_tr td:nth-child(2)")
        # 把元素列表 转换为名称列表，使用列表推导式（python-列表）
        member_list = [ele.text for ele in ele_list]
        # 成员的名称的列表
        return member_list