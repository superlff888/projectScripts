# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:11
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""登录"""

from CTTQ.dcsqas.web.base.base_page import BasePage
from CTTQ.dcsqas.web.gateCenterAI.gateAI import GateAILink, GateAIServer_machineVision, Phonetic_language


class Login(BasePage):

    def login(self, obj):
        """
        by_*   元组或列表参数
        """
        by_account, text_account, by_password, text_password, by_click = obj
        self.fond(by_account).send_keys(text_account)
        self.fond(by_password).send_keys(text_password)
        self.fond(by_click).click()
        return GateAIServer_machineVision(self.driver), Phonetic_language(self.driver), GateAILink(self.driver)  # BasePage构造方法防止再次打开一个网页
