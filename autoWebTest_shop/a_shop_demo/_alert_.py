# -*- coding=utf-8 -*-
# @Time    : 2023/02/19 09:00
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from common.driver import element_click_success

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_js_alert")
driver.switch_to.frame("iframeResult")  # 通过id或name直接切换到iframe
WebDriverWait(driver, 10, 0.1).until(element_click_success(By.XPATH, "//*[text()='试一试']"))

# 切换到alert弹框（frame框架中的弹框）
alert = driver.switch_to.alert
print(alert.text)
sleep(2)
alert.accept()  # 点击确定
driver.quit()