# -*- coding=utf-8 -*-
# @Time    : 2023/02/09 13:46
# @Author  : ╰☆H.俠ゞ
# =============================================================


import allure
import pytest


def pytest_collection_modifyitems(items):
    """
    该hook函数可防止allure少收集模块的用例
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    ::return : None
    """
    for item in items:  # item 为执行的每条用例
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")
