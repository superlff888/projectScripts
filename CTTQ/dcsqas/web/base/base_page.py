# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 18:13
# @Author  : ╰☆H.俠ゞ
# =============================================================


import logging
import os

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import with_tag_name
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage:
    """
    封装一些和业务无关的重复代码
    是某些操作的底层
    """

    def __init__(self, base_driver: WebDriver = None, url: str = None):
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

    def clicked(self, by, locator=None):
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
            return self.driver.find_element(*by).click()  # 解包
        else:
            # 如果传入两个参数，则正常使用。
            return self.driver.find_element(by, locator).click()

    def send_file(self, value, by, locator=None):
        """
        有可能传入 的是一个元祖(a, b)
        也有可能是传入两个参数
        ::value: filename.jpg ;文本、文件绝对路径、图片绝对路径,推荐os.path.abspath("1.jpg")
        ::param by:
        ::param locator:
        ::return:
        """
        # print(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
        # logging.debug(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
        path = os.path.abspath(value)
        if locator is None:
            # 如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_element(*by).send_keys(path)  # 解包
        else:
            # 如果传入两个参数，则正常使用。
            return self.driver.find_element(by, locator).send_keys(path)

    def send(self, value, by, locator=None):
        """
        有可能传入 的是一个元祖(a, b)
        也有可能是传入两个参数
        ::value: filename.jpg ;文本、文件绝对路径、图片绝对路径,推荐os.path.abspath("1.jpg")
        ::param by:
        ::param locator:
        ::return:
        """
        # print(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")
        # logging.debug(f"元素的定位方式为{by}， 元素的定位表达式为{locator}")

        if locator is None:
            # 如果传入元祖，那么给元祖做解包，分别传入到函数中
            return self.driver.find_element(*by).send_keys(value)  # 解包
        else:
            # 如果传入两个参数，则正常使用。
            return self.driver.find_element(by, locator).send_keys(value)

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
        """by is a list or tuple"""
        ele = self.driver.find_elements(by)
        list_a = []
        for i in ele:
            text = i.text
            list_a.append(text)
        return list_a

    def get_text(self, by):
        return self.driver.find_element(by).text

    def below_s4(self, ag_name, element_or_locator):
        """返回指定元素下方的元素 https://blog.csdn.net/qq_18298049/article/details/117194464"""
        self.driver.find_element(with_tag_name(ag_name).below(element_or_locator))

    def WebDriverWait_until_clickable(self, timeout, ele):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(ele))
        # except NoSuchElementException:
        #     return self.search(obj)
        # except ElementClickInterceptedException:
        #     return self.search(obj)
        # except WebDriverException:
        #     return self.search(obj)
        # except ElementNotVisibleException:
        #     return self.search(obj)
        # except Exception as e:
        #     print(f"抛出异常{e}")
        #     return self.search(obj)

    # def miss(self, close_bn):
    #     try:
    #         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(close_bn))
    #         self.fond(close_bn).click()
    #         self.fond(close_bn)
    #         return self.search, self.fond, self.driver
    #     except ElementClickInterceptedException:
    #         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(close_bn))
    #         return self.miss(close_bn)
    #     except Exception:
    #         WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(close_bn))
    #         return self.miss(close_bn)