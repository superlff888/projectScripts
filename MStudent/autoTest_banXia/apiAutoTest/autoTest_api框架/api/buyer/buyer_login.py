# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

import requests

from autoTest_banXia.apiAutoTest.autoTest_api框架.common.httpReuquests import HttpRequest, httpRequestCookies


class BuyerLoginApi:
    def __init__(self):
        self.url = "http://www.mtxshop.com:7002/passport/login"
        self.method = "post"
        self.params = {
            "username": "mtx0327",
            "password": "fcea920f7412b5da7be0cf42b8c93759",
            "captcha": "1512",
            "uuid": "f6597380-4e24-11ed-984b-167610639c7"
        }

    def send(self):
        self.res = httpRequestCookies.request(url=self.url, method=self.method, params=self.params)
        return self.res


if __name__ == "__main__":
    b = BuyerLoginApi()
    pprint(b.send().json())  # 状态码
