# -*- coding=utf-8 -*-
# @Time    : 2022/09/01 16:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class TestCas:

    def test_search(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ainewqas.cttq.com/cvue/SunnyShop-WebPC")
        self.driver.implicitly_wait(3)
        self.driver.find_element(By.ID, "login-workcode").send_keys("8106139")
        self.driver.find_element(By.ID, "login-password").send_keys("cttq.1234")
        self.driver.find_element(By.ID, "login-btn").click()

        WebDriverWait(self.driver, 20). \
            until(ec.element_to_be_clickable((By.CSS_SELECTOR,
                                              "body > div.cttq-guide-page > div > div > div.el-dialog__body > div.close")))
        self.driver.find_element(By.CSS_SELECTOR,
                                 "body > div.cttq-guide-page > div > div > div.el-dialog__body > div.close").click()

        self.driver.find_element(By.XPATH, "//input[@placeholder='请输入商品名、品牌、CAS号、货号']").send_keys("华为")
        text = self.driver.find_element(By.XPATH, "/html/body/section/div/header/div[2]/div[1]/span").text
        print(self.driver.find_element(By.XPATH, "/html/body/section/div/header/div[2]/div[1]/span"))
        print(f"获取的元素text:{text}")

