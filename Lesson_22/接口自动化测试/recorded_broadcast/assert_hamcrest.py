# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 15:43
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
复杂规则断言
"""
from pprint import pprint

import requests
from hamcrest import *
from jsonpath import jsonpath


class TestDemo:
    def test_jsonpath(self):
        r = requests.get('https://ceshiren.com/categories.json')
        # pprint(jsonpath(r.json(), '$..name'))  # $..name递归深度遍历，获取子孙路径的 name;# jsonpath传递的参数必须是json obj
        print(type(jsonpath(r.json(), '$..name')[0]))
        assert_that(jsonpath(r.json(), '$..name')[0], contains_string('开源项'))  # 真实结果 匹配器



