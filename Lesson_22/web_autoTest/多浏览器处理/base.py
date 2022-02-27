# -*- coding=utf-8 -*-
# @Time    : 2022/02/27 10:32
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""

命令行用setup
非命令行用init方法
"""

from selenium import webdriver
import os


class Base:

   def setup(self):
       """
       处理多浏览器
       :return:
       """
       browser = os.getenv("browser")
       if browser == "firefox":
           self.driver = webdriver.Firefox()
       elif browser == "headless":
           self.driver == webdriver.PhantomJS()
       elif browser == "chrome":
           self.driver = webdriver.Chrome()
       self.driver.maximize_window()
       self.driver.implicitly_wait(5)

   def teardown(self):
       self.driver.quit()

