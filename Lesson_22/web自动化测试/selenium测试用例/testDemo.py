# -*-coding=utf-8-*-
# @Time   : 2022/02/16 20:51
# @Author : ®t°ÓH.Çb©g
# =============================================================

from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium import webdriver


class TestHogwarts:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_selenium(self):
        self.driver.get("https:baidu.com")
        self.driver.find_element_by_css_selector("#kw").send_keys("—ßœ∞")
        self.driver.find_element_by_css_selector("#su").click()


