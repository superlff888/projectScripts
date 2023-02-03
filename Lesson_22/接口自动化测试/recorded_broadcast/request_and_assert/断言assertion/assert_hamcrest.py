# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 15:43
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
复杂规则断言
"""
from pprint import pprint

import requests
# unittest 断言方式
from hamcrest import *
from jsonpath import jsonpath


class TestDemo:
    def test_jsonpath(self):
        r = requests.get('https://ceshiren.com/categories.json')
        print(r.json())
        print(f"r.json()的类型为：{type(r.json())}")
        print(type(r.text))
        print(r.text)
        print(type(r.content))
        print(r.content)
        # pprint(jsonpath(r.json(), '$..name'))  # $..name递归深度遍历，获取子孙路径的 name;# jsonpath传递的参数必须是json obj
        print(f"jsonpath(r.json(), '$..name')[0])的类型：{type(jsonpath(r.json(), '$..name')[0])}")
        print(f"jsonpath(r.json(), '$..name')[0])为：{jsonpath(r.json(), '$..name')[0]}")
        print(f"jsonpath(r.json(), '$..name'))为：{jsonpath(r.json(), '$..name')}")
        assert_that(jsonpath(r.json(), '$..name')[1], contains_string('开源项目'))  # 真实结果 匹配器
        assert_that(jsonpath(r.json(), '$..name'), has_item("开源项目"))  #


