# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 10:11
# @Author  : ╰☆H.俠ゞ
# =============================================================

from CTTQ.dcsqas.web.base.base_page import BasePage
from CTTQ.dcsqas.web.gateCenterAI.gateAI import GateAIServer100, GateAIServer200, GateAIServer300, GateAIServer400, \
    GateAIServer500, GateAILink


class Login(BasePage):

    def login(self, obj):
        """
        by_*   元组或列表参数
        """
        by_account, text_account, by_password, text_password, by_click = obj
        self.fond(by_account).send_keys(text_account)
        self.fond(by_password).send_keys(text_password)
        self.fond(by_click).click()
        return GateAIServer100(
            self.driver), GateAIServer200(), GateAIServer300(), GateAIServer400(), GateAIServer500(), GateAILink()  # BasePage构造方法防止再次打开一个网页
