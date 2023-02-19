# -*- coding=utf-8 -*-
# @Time    : 2023/02/19 09:28
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def radio_buttons():
    """单选框"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_radiobuttons")
    driver.maximize_window()
    # driver.switch_to.frame("iframeResult")  # 通过id或name直接切换
    driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))  # 通过元素切换
    if driver.find_element(By.CSS_SELECTOR, "[value='male']").is_selected():  # 判断是否可选择
        if driver.find_element(By.CSS_SELECTOR, "[value='female']").is_enabled():  # 判断是否可使用
            driver.find_element(By.CSS_SELECTOR, "[value='female']").click()
    # driver.quit()  # 退出浏览器


def checkboxes():
    """复选框"""
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_checkboxes")
    driver.maximize_window()
    # driver.switch_to.frame("iframeResult")  # 通过id或name直接切换
    driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))  # 通过元素切换
    if not driver.find_element(By.CSS_SELECTOR, "[name='Bike']").is_selected():  # 判断是否被选中
        if driver.find_element(By.CSS_SELECTOR, "[name='Bike']").is_enabled():
            driver.find_element(By.CSS_SELECTOR, "[name='Bike']").click()
            sleep(3)
    print("清除复选中……")
    driver.switch_to.default_content()  # 通过元素切换
    driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))  # 通过元素切换
    driver.find_element(By.CSS_SELECTOR, "[name='Bike']").click()
    print("已清除复选")
    sleep(3)
    driver.quit()  # 退出浏览器


def dropdown_box():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get("https://www.w3school.com.cn/tiy/t.asp?f=eg_html_dropdownbox")
    driver.maximize_window()
    # driver.switch_to.frame("iframeResult")  # 通过id或name直接切换
    driver.switch_to.frame(driver.find_element(By.ID, "iframeResult"))  # 通过元素切换

    ele = driver.find_element(By.CSS_SELECTOR, "[name='cars']")
    select = Select(ele)
    select.select_by_value("saab")
    # select.select_by_visible_text("Saab")
    # select.select_by_value("audi")
    sleep(3)


if __name__ == '__main__':
    # checkboxes()
    dropdown_box()