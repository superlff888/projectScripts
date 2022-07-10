# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 16:52
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests
from requests.auth import HTTPBasicAuth
# params = {
#     "user": "banana",
#     "password": "123"
#           }


def test_auth():
    r = requests.get(url="https://httpbin.testing-studio.com/basic-auth/banana/123",
                     auth=HTTPBasicAuth("banana", "123"))
    print(r.text)
    print(r.content)
    print(r.status_code)
    print(r.headers)
    print(r.json())
