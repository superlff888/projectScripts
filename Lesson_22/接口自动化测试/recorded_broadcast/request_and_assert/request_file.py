# -*- coding=utf-8 -*-
# @Time    : 2022/07/08 21:05
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests


class F:

    def test_file(self):
        url = "https://httpbin.testing-studio.com/post"
        file = {"file": "open('reports.xls','rb')"}
        r = requests.post(url=url, files=file)
        print(r.json())