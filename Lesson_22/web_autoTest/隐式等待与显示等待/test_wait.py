# -*- coding=utf-8 -*-
# @Time    : 2022/02/17 20:12
# @Author  : ╰☆H.俠ゞ
# =============================================================
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:
    """
    locator ！= element
    locator 定位器  就是 ： “(By.ID, value)”  注意：一定要带括号
    element 元素 value
    on_element  代表 ： “driver.find_element(By.ID, value)”
    """

    def setup(self):
        self.driver = webdriver.Chrome()  # 要配置chromedriver驱动的环境变量
        self.driver.get("https://ceshiren.com/")
        self.driver.maximize_window()
        # 自动每隔0.5秒轮询查找元素；全局等待(self.driver.implicitly)，作用于所有find_element,只要在设定时间内有元素定位不到就抛异常
        # self.driver.implicitly_wait(5)

    def test_wait(self):
        # until()方法中要传一个f方法method，即函数
        # 元素存在presence，但元素默认是隐藏
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#ember31")))
        # 可见visibility，但可能还没加载完
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[id="ember31"]')))

        # 自定义一个方法
        def wait(x):  # 方法中一定要带一个参数，因为until中会将self._driver传给该方法
            return len(self.driver.find_elements(By.CSS_SELECTOR, "#ember31")) >= 1  # 判断元素的个数（长度）
        """
        value = wait(self._driver)  # 
                if value:  # 判断比较运算是否为真 ，概念模糊的话，print(2>1) ,比较运算的返回值为 True
                    return value
        """
        WebDriverWait(self.driver, 5).until(wait)  # 传入方法名，不要带括号;而且此方法返回值为真，脚本才会结束等待，继续执行下面的代码
        self.driver.find_element(By.CSS_SELECTOR, "#ember31").click()
        print(self.driver.find_element(By.CSS_SELECTOR, "#ember31").location)  # {'x': 371, 'y': 75}

