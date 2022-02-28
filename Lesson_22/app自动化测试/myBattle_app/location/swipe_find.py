# -*- coding=utf-8 -*-
# @Time    : 2022/02/25 10:19
# @Author  : ╰☆H.俠ゞ
# =============================================================


# 定义加滑动边查找的方法
import logging

from appium.webdriver.common.mobileby import MobileBy
from selenium.common.exceptions import NoSuchElementException


def swipe_find_leftAndRight(driver, element, location):
    """
    left and right
    横向滑动
    """
    # 获取滑动的元素坐标点
    lc = element.location
    # 获取滑动元素的大小
    size = element.size
    # 初始化元素坐标点的值
    x = lc['x']
    y = lc['y']
    w = size['width']
    h = size['height']
    start_x = x + w / 2
    start_y = y + h / 5
    end_x = x + w / 3
    end_y = start_y

    while True:
        page = driver.page_source  # 获取当前窗口的资源
        try:
            driver.find_element(*location).click()  # 点击对应的频道信息
            return True
        except Exception as e:
            logging.debug(f"debug:{e}")
            driver.swipe(start_x, start_y, end_x, end_y, duration=2000)  # 滑动页面(横向滑动),滑动时间2秒
        if driver.page_source == page:  # 最后划不动了，所以刷新的页面没有变化
            print("已经滑动到最后页面，没有找到对应的元素信息!")
            logging.debug("已经滑动到最后页面，没有找到对应的元素信息!")
            return False


def swipe_fond(self, text, num=3):  #
    """
    滑动查找目标元素的text
    根据滑动的距离，可预置滑动的次数
    滑动时间为2000ms
    Up and down
    """
    for i in range(num):
        try:
            element = self.driver.find_element(MobileBy.XPATH, f"//*[@text='{text}']")
            logging.debug(f"已经找到目标元素对应的text：{text}")
            return element
        except Exception as e:
            print("未找到")
            logging.debug(f"debug:{e}")
            size = self.driver.get_window_size()  # 获取当前屏幕的尺寸（不同设备，坐标不同，可能无法滑动）
            # 'width', 'height'
            width = size.get("width")
            height = size.get("height")
            start_x = width / 2
            start_y = height * 0.8
            end_x = start_x
            end_y = height * 0.3
            self.driver.swipe(start_x, start_y, end_x, end_y, duration=2000)
        if i == num - 1:
            raise NoSuchElementException(f"找了{num}次，未找到元素")  # 次数用完，抛异常NoSuchElement
