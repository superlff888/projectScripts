# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

import pytest

from selenium.webdriver.common.by import By

from CTTQ.dcsqas.page_object.login_dcs import Login
import sys


# sys.path.append("D:\Develop\git_pub_repositories\projectScripts")  # （运行程序时）添加path环境变量


class TestCas:

    def setup_class(self):
        self.lg = Login(url="https://ainewqas.cttq.com/cvue/SunnyShop-WebPC")
        self.lg.win_max()
        self.searched = self.lg.login([(By.ID, "login-workcode"), "8106139",
                                       (By.ID, "login-password"), "cttq.1234", (By.ID, "login-btn")]) \
            .miss((By.XPATH, "//div[@class='el-dialog__body']/div[3]"))  # 关闭提示框/html/body/div[1]/div/div/div[2]/div[3]

    def test_search(self):
        self.searched([(By.XPATH,
                        "//input[@placeholder='请输入商品名、品牌、CAS号、货号']"), "华为",
                       (By.XPATH,
                        "//div[@class='el-input-group__append']/button[@class='el-button el-button--default']")])
        # "/html/body/section/section/section/main/div/div[1]/div/header/div[2]/div[1]/div[1]/div/button"
        # 获取商品名列表
        pytest.assume(1 == 1)
