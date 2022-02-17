# -*- coding=utf-8 -*-
# @Time    : 2022/02/17 09:08
# @Author  : ╰☆H.俠ゞ
# =============================================================

from selenium import webdriver


class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_selenium(self):
        self.driver.get("https:baidu.com")
        self.driver.find_element_by_css_selector("#kw").send_keys("自动化测试框架")
        self.driver.find_element_by_css_selector("#su").click()