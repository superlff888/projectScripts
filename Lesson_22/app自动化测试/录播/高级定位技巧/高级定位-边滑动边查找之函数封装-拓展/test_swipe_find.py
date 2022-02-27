# -*- coding=utf-8 -*-
# @Time    : 2022/02/25 10:19
# @Author  : ╰☆H.俠ゞ
# =============================================================


# 定义加滑动边查找的方法
def swipe_find(driver, element, location):
    # 获取滑动的元素坐标点
    lc = element.location
    # 获取滑动元素的大小
    size = element.size
    # 初始化元素坐标点的值
    x = lc['x']
    y = lc['y']
    w = size['width']
    h = size['height']
    startx = x + w * 0.9
    starty = y + h/2
    endx = x + w * 0.1
    while True:
        page = driver.page_source   # 获取的是整个app页面的信息
        try:
            driver.find_element(*location).click()  # 点击对应的频道信息
            return True
        except Exception as e:
            driver.swipe(startx, starty, endx, starty, duration=2000)  # 滑动页面
        if driver.page_source == page:  # 刷新页面后，
            print("已经滑动到最后页面，没有找到对应的频道信息!")
            return False
