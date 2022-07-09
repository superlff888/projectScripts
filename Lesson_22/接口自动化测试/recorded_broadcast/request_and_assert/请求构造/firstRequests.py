# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 10:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
接口自动化演练环境
https://httpbin.testing-studio.com/
"""
from pprint import pprint

import requests


class Test_demo:
    def test_get_demo(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.text)
        print(r.request.method)
        print(r.request.body)
        print(r.json())
        assert r.request.method == 'GET'

    def test_post_demo(self):
        # post请求
        payload = {
            "level": 1,
            "name": "lee"
            }
        r = requests.post(url="https://httpbin.testing-studio.com/post", json=payload)
        # pprint(r.json())
        pprint(r.request)
        pprint(r.headers)
