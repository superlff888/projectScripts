# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:13
# @Author  : ╰☆H.俠ゞ
# =============================================================


import logging
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.relative_locator import with_tag_name


class BasePage:
    """
    封装一些和业务无关的重复代码
    是某些操作的底层
    """

    def __init__(self, base_driver: WebDriver = None, url=None):
        self._BASE_URL = url  # 类变量要大写；私有化属性

        if base_driver is None:
            # 实例化
            self.driver = webdriver.Chrome()  # 打开一个浏览器 ，WebDriver Object
            # 添加隐式等待的配置【全局】
            self.driver.implicitly_wait(3)
        else:
            self.driver: WebDriver = base_driver
        if self._BASE_URL != "":  # 子类隔代继承；属性私有化，目的不把内部元素暴漏给外部（预防被修改）
            try:
                self.driver.get(self._BASE_URL)
                self.driver.implicitly_wait(3)
            except Exception as e:
                print(f"url填写错误{e}")
                logging.info(f"url填写错误{e}")

    def fond(self, by, locator=None):  # 兼容元组
        """
        有可能传入 的是一个元祖(a, b)
        也有可能是传入两个参数
        :param by:
        :param locator:
        :return:
        """
        # print(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
        # logging.debug(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
        if locator is None:
            # 如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_element(*by)  # 解包
        else:
            # 如果传入两个参数，则正常使用。
            return self.driver.find_element(by, locator)

    def closed(self):
        self.driver.close()

    def win_max(self):
        self.driver.maximize_window()

    def text_list(self, by):
        ele = self.driver.find_elements(by)
        list_a = []
        for i in ele:
            text = i.text
            list_a.append(text)
        return list_a

    def below_s4(self, ag_name, element_or_locator):
        """返回指定元素下方的元素 https://blog.csdn.net/qq_18298049/article/details/117194464"""
        self.driver.find_element(with_tag_name(ag_name).below(element_or_locator))