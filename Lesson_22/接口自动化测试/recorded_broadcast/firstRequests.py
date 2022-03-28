# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 10:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
接口自动化演练环境
https://httpbin.testing-studio.com/
"""
import requests


class Test_demo:
    def test_demo(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        # print(r.text)
        print(r.request.method)
        assert r.request.method == 'GET'