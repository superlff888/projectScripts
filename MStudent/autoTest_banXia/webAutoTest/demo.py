# -*- coding=utf-8 -*-
# @Time    : 2023/02/08 13:54
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("http://www.mtxshop.com:3000/login")
sleep(2)
driver.maximize_window()
sleep(3)
driver.find_element(By.PARTIAL_LINK_TEXT, '账号登录').click()
sleep(1)
driver.find_element(By.XPATH, "//*[@id='username' and @placeholder='邮箱/用户名/已验证手机']").send_keys("leeseller")
driver.find_element(By.XPATH, "//*[@id='password']").send_keys("123456")
driver.find_element(By.XPATH, "//*[@id='validcode']").send_keys("1512")
driver.find_elements(By.XPATH, "//*[@class='form-sub']")[1].click()
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//*[@class='to-member' and text()='进入个人中心']").click()
driver.implicitly_wait(1)
# driver.find_element(By.XPATH, "//*[@href='/member/shipping-address' and text()='收货地址']").click()
driver.find_element(By.XPATH, "//*[text()='收货地址' and @href='/member/shipping-address']").click()
driver.implicitly_wait(1)
driver.find_element(By.XPATH, "//*[@class='el-button add-address-btn el-button--default el-button--mini']").click()

# driver.close()

WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located('locator'))
s = Select('ele')
s.select_by_index("")

js = "document.getElementByClassName('').removeAttribute('readonly')"
driver.find_element('locator').clear()
windows = driver.window_handles
driver.switch_to.window(windows[1])
driver.switch_to.window("")


driver.get_cookie()

