# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 20:48
# @Author  : ╰☆H.俠ゞ
# =============================================================


"""
selenium复杂操作 示例： 在百度页面中，进入搜索设置中，修改提示不显示，每页显示条数为50条
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


driver = webdriver.Firefox()
driver.get('https://www.baidu.com')


setting = driver.find_element_by_link_text('设置')
ac = ActionChains(driver)
ac.move_to_element(setting).perform()

driver.find_element_by_link_text('搜索设置').click()

# 定位到下拉框
s = driver.find_element_by_id('nr')
# #创建一个select类对象
select = Select(s)

# 根据下标选择下拉选项
select.select_by_index(2)
# # 根据select标签中的option标签的value值选择下拉选项
# select.select_by_value('50')
# # 根据下拉选项的文本内容选择
# select.select_by_visible_text('每页显示50条')