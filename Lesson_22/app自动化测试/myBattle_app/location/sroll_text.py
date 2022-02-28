# -*- coding=utf-8 -*-
# @Time    : 2022/02/27 20:05
# @Author  : ╰☆H.俠ゞ
# =============================================================
from appium.webdriver.common.mobileby import MobileBy


def scroll_text(text):
    # 把想要查找的text文本输入text("")中
    locator = (MobileBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true).instance(0)).'
                                             'scrollIntoView(new UiSelector().text(text).instance(0));')
    return locator