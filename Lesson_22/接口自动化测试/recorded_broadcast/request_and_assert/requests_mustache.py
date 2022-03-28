# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 13:35
# @Author  : ╰☆H.俠ゞ
# =============================================================


import requests
import pystache  # 用两个花括号识别变量，可以对变量自动识别和替换


class TestDemo:
    def test_demo(self):
        j = pystache.render("Hi,{{person}}!", {"person": "lee"})  # 返回给定模板字符串，即template参数
        print(j)

