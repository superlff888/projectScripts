# -*- coding=utf-8 -*-
# @Time    : 2022/02/19 22:04
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import time
from time import sleep

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as e
from selenium.webdriver.support.wait import WebDriverWait

"""
【模拟鼠标和键盘操作】
    1、调用ActionChains()的方法时，不会立即执行，而是将所有的操作放在一个队列里，当调用perform()方法时，队列中的事件将会依次执行
    2、调用方法：链式调用、分布调用
    3、页面的大小和位置固定，在此特定位操作鼠标，移动元素位置
"""


class Test_ActionChains:
    """
    测试类中不可以有init构造函数
    """
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown(self):
        """
        driver.quit() 关闭自动化测试软件打开的所有窗口
        driver.close() 仅关闭当前窗口
        """
        self.driver.quit()  # 关闭自动化测试软件打开的所有窗口

    # 1、鼠标点击练习地址 https://sahitest.com/demo/clicks.htm
    @pytest.mark.skip  # 跳过
    def test_case_click(self):
        """
        locator = (strategy + element)
        :strategy: 定位策略
        """
        self.driver.get('https://sahitest.com/demo/clicks.htm')
        self.action = ActionChains(self.driver)
        # until中入参为locator，是一个元组(By.XPATH, '//input[@value="click me"]')
        WebDriverWait(self.driver, 10).until(e.element_to_be_clickable((By.XPATH, '//input[@value="click me"]')))
        # on_element
        ele_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        WebDriverWait(self.driver, 10).until(e.element_to_be_clickable((By.XPATH, '//input[@value="dbl click me"]')))
        ele_click_dbl = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        WebDriverWait(self.driver, 10).until(e.element_to_be_clickable((By.XPATH, '//input[@value="right click me"]')))
        ele_click_right = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        # 链式调用,参数：on_element is “self.driver.find_element(By.XPATH, element)”
        self.action.click(ele_click).double_click(ele_click_dbl).context_click(ele_click_right).perform()
        # 分布调用
        # self.action.click('//input[@value="click me"]')
        # self.action.click(ele_click)
        # self.action.double_click(ele_click_dbl)
        # self.action.context_click(ele_click_right)
        # sleep(2)
        # self.action.perform()
        sleep(2)

    @pytest.mark.skip
    # 鼠标移动到某个元素上 (适用于未点击该元素情况下，自动弹出下拉菜单)
    def test_moveToElement(self):
        self.driver.get("http://www.baidu.com")  # 打开百度
        self.action = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(e.visibility_of_element_located((By.CSS_SELECTOR, "#s-usersetting-top")))  # until参数：locator
        to_element = self.driver.find_element(By.CSS_SELECTOR, "#s-usersetting-top")  # to_element
        self.action.move_to_element(to_element)  # to_element is “self.driver.find_element(By.XPATH, element)”
        self.action.perform()  # 所有鼠标操作切记不要忘记执行
        sleep(5)

    @pytest.mark.skip
    # 拖拽到目标元素
    def test_drag_and_drop(self):
        self.driver.get("https://sahitest.com/demo/dragDropMooTools.htm")
        self.action = ActionChains(self.driver)
        WebDriverWait(self.driver, 10).until(e.visibility_of_element_located((By.CSS_SELECTOR, "#dragger")))  # until参数：locator
        drag_ele = self.driver.find_element(By.CSS_SELECTOR, "#dragger")
        WebDriverWait(self.driver, 10).until(e.visibility_of_all_elements_located((By.CSS_SELECTOR, "#dragger")))  # until参数：locator
        drop_ele = self.driver.find_elements(By.CSS_SELECTOR, ".item")
        print(f'\n获得的元素列表为：\n{drop_ele}')
        print(f'定位元素个数：{len(drop_ele)}')
        drop_ele_1 = drop_ele[0]
        drop_ele_2 = drop_ele[1]
        drop_ele_3 = drop_ele[2]
        drop_ele_4 = drop_ele[3]
        # # 方法1
        # self.action.drag_and_drop(drag_ele, drop_ele_1).perform()
        # sleep(1)
        # self.action.drag_and_drop(drag_ele, drop_ele_2).perform()
        # sleep(1)
        # self.action.drag_and_drop(drag_ele, drop_ele_3).perform()
        # sleep(1)
        # self.action.drag_and_drop(drag_ele, drop_ele_4).perform()
        # sleep(1)

        # 方法2 鼠标左键长按元素drag_ele，移动元素drag_ele至元素drop_ele_1，并释放在drop_ele_1元素位置
        self.action.click_and_hold(drag_ele).move_to_element(drop_ele_1).release(drop_ele_1).perform()
        sleep(1)
        self.action.click_and_hold(drag_ele).move_to_element(drop_ele_1).release(drop_ele_2).perform()
        sleep(1)
        self.action.click_and_hold(drag_ele).move_to_element(drop_ele_1).release(drop_ele_3).perform()
        sleep(1)
        self.action.click_and_hold(drag_ele).move_to_element(drop_ele_1).release(drop_ele_4).perform()
        sleep(1)

    def test_Keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        self.action = ActionChains(self.driver)  # 注意：不同的URL，对应不同的action
        WebDriverWait(self.driver, 10).until(e.visibility_of_element_located((By.CSS_SELECTOR, 'label>input[type="textbox"]')))
        location = self.driver.find_element(By.CSS_SELECTOR, 'label>input[type="textbox"]').location  # 获取元素坐标
        print(location)
        element = self.driver.find_element(By.CSS_SELECTOR, 'label>input[type="textbox"]')
        print(element)
        element.click()  # 设想真实键盘操作，必须先click点击该元素locator，将光标定位于此 （注意区别于webelement的 “element.send_keys()”）
        sleep(3)
        # 分布键入内容
        self.action.send_keys("house").pause(2)  # 键入内容
        self.action.send_keys(Keys.SPACE).pause(2)  # 空格
        self.action.send_keys("lee").pause(1)
        self.action.send_keys(Keys.BACKSPACE).perform()
        now_time = time.strftime('%Y%m%d%H%M%S', time.localtime())  # 当前时间转化为字符串
        # 获取当前文件的根目录(D:\Develop\git_pub_repositories\projectScripts\Lesson_22\web_autoTest\web控件 - ActionChains)，再做字符串拼接
        self.driver.save_screenshot(os.path.dirname(__file__) + f'/{now_time}.png')
        sleep(3)

        """
        组合键
        send_keys(Keys.BACK_SPACE)   删除键（BackSpace） 
        send_keys(Keys.SPACE)        空格键(Space) 
        send_keys(Keys.TAB)          制表键(Tab) 
        send_keys(Keys.ESCAPE)       回退键（Esc） 
        send_keys(Keys.ENTER)        回车键（Enter） 
        send_keys(Keys.CONTROL,'a')  全选（Ctrl+A） https://blog.csdn.net/chuanshixx/article/details/106900443
        send_keys(Keys.CONTROL,'c')  复制（Ctrl+C） https://blog.csdn.net/chuanshixx/article/details/106900443
        send_keys(Keys.CONTROL,'v')  粘贴（Ctrl+V） https://blog.csdn.net/chuanshixx/article/details/106900443
        send_keys(Keys.CONTROL,'x')  剪切（Ctrl+X） https://blog.csdn.net/chuanshixx/article/details/106900443
        """








