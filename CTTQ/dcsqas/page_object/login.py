# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:11
# @Author  : ╰☆H.俠ゞ
# =============================================================
from CTTQ.dcsqas.page_object.base_page import BasePage
from CTTQ.dcsqas.page_object.search import Search


class Login(BasePage):

    _BASE_URL = "https://ssoqas.cttq.com/login"

    def login(self, by):
        self.fond(by)
        return Search