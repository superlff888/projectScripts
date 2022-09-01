# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

import pytest
from selenium.webdriver.common.by import By
from CTTQ.dcsqas.page_object.login_dcs import Login


class TestCas:

    def setup_class(self):
        self.lg = Login(url="https://ainewqas.cttq.com/cvue/SunnyShop-WebPC")
        self.lg.win_max()

    def test_search(self):
        self.lg.login([(By.ID, "login-workcode"), "8106139",
                       (By.ID, "login-password"), "cttq.1234", (By.ID, "login-btn")]).\
            search([(By.XPATH,
                    "//input[@placeholder='请输入商品名、品牌、CAS号、货号']"), "华为",
                   (By.XPATH, "/html/body/section/section/section/main/div/div[1]/div/header/div[2]/div[1]/div[1]/div/button"),
                   (By.XPATH, "/html/body/div[1]/div/div/div[2]/div[3]")])
        # 获取商品名列表
        pytest.assume(1 == 1)


