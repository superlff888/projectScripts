# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 14:56
# @Author  : ╰☆H.俠ゞ
# =============================================================f
from pprint import pprint  # 格式化
import requests
from jsonpath import jsonpath


class TestDemo:
    def test_jsonpath(self):
        r = requests.get('https://ceshiren.com/categories.json')
        # jsonpath传递的参数必须是json object
        pprint(jsonpath(r.json(), '$..name'))  # $..name递归深度遍历，获取子孙路径的 name
        assert jsonpath(r.json(), '$..name')[1] == '开源项目'

