# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:11
# @Author  : ╰☆H.俠ゞ
# =============================================================
from selenium.webdriver.common.by import By

from cttq.dcsqas.page_object.base_page import BasePage
from cttq.dcsqas.page_object.homePage import HomePage


class Login(BasePage):
    # _BASE_URL = "https://ainewqas.cttq.com/cvue/SunnyShop-WebPC"

    def login(self, obj):
        """
        by_*   元组或列表参数
        """
        by_account, text_account, by_password, text_password, by_click = obj
        self.fond(by_account).send_keys(text_account)
        self.fond(by_password).send_keys(text_password)
        self.fond(by_click).click()
        return HomePage(self.driver)  # 又打开一个网页

