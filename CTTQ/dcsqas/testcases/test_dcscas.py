# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
from time import sleep

import pytest
from selenium.webdriver.common.by import By

from CTTQ.dcsqas.page_object.login_dcs import Login


class TestCas:

    def setup_class(self):
        self.lg = Login(url="https://ainewqas.cttq.com/cvue/SunnyShop-WebPC")
        self.lg.win_max()
        self.searched, self.fond, self._driver = self.lg.login([(By.ID, "login-workcode"), "8106139",
                                       (By.ID, "login-password"), "cttq.1234", (By.ID, "login-btn")]) \
            .miss((By.XPATH, "//div[@class='el-dialog__body']/div[3]"))  # 关闭提示框

    def test_search(self):
        self.searched([(By.XPATH, "//input[@placeholder='请输入商品名、品牌、CAS号、货号']"), "华为",
                       (By.XPATH,
                        "//div[@class='el-input-group__append']/button[@class='el-button el-button--default']")])
        self._driver.implicitly_wait(1)
        self.fond((By.XPATH, "//input[@placeholder='请输入商品名、品牌、CAS号、货号']")).clear()  # 清空单元格

        # 获取商品名列表
        pytest.assume(1 == 1)


if __name__ == "__main__":
    os.system("pytest -sv test_dcscas.py")