# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import unittest
import pytest
from selenium.webdriver.common.by import By

from CTTQ.dcsqas.web.gateCenterAI.login_dcs import Login


class TestCas(unittest.TestCase):

    def setup_class(self):
        self.lg = Login(url="https://ainewqas.cttq.com/cvue/SunnyShop-WebPC")
        self.lg.win_max()
        self.gmv, self.pl, self.gl = self.lg.login([(By.ID, "login-workcode"), "8102784",
                                                    (By.ID, "login-password"), "cttq.1234",
                                                    (By.ID, "login-btn")])
        self.lg.implicitly_time(3)

    def test_IDci(self, obj: tuple, value, by_card: tuple, by_text: tuple):
        self.gmv.identity_card(obj).ID_card_identification(value, by_card)
        self.lg.WebDriverWait_until_clickable(10, (By.ID, "target"))
        text = self.lg.get_text(by_text)
        self.assertIn(text, ("姓名", "身份证"))


if __name__ == "__main__":
    os.system("pytest -sv test_dcscasAI.py")
