# -*- coding=utf-8 -*-
# @Time    : 2022/02/17 20:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep
from selenium import webdriver


class testWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://ceshiren.com/")

    def test_wait(self):
        sleep(3)
        print("hello")

