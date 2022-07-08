# -*- coding=utf-8 -*-
# @Time    : 2022/07/08 21:13
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests


class Test_Headers:

    def test_headers(self):
        headers = {'user-agent': 'my-app/0.0.1'}
        r = requests.get(url="https://httpbin.testing-studio.com/get", headers=headers)
        print(r.text)

