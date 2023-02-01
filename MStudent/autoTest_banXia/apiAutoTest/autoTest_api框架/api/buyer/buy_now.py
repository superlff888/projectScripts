# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 11:46
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

import requests

from autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.base_buyer import BaseBuyerApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buyer_login import BuyerLoginApi


class BuyNowApi(BaseBuyerApi):  # 业务成功将订单信息存入redis

    def __init__(self):
        # 把父类的属性拿来为我所用，可以直接用，也可重新复制
        super().__init__()  # 【继承】可以继承父类的类属性和方法(包括__init__构造方法)，但不能直接继承实例属性； 同BaseBuyerApi().__init__()
        self.url = f"{self.host}/trade/carts/buy"
        self.method = "post"
        self.res = None
        # self.header = {"Authorization": self.buyer_token}  #
        self.params = {
            "sku_id": 600,
            "num": 1
        }

    def send(self):
        session = requests.sessions.Session()
        self.res = session.request(url=self.url, method=self.method, params=self.params, headers=self.header)
        return self.res


if __name__ == '__main__':
    params = {
        "username": "mtx0327",
        "password": "fcea920f7412b5da7be0cf42b8c93759",
        "captcha": "1512",
        "uuid": "f6597380-4e24-11ed-984b-167610639c7"
    }
    b = BuyerLoginApi("http://www.mtxshop.com:7002/passport/login", "post", params)
    pprint(b.send().json())  # 状态码
    # token = res.json()["access_token"]
    # BaseBuyerApi.buyer_token = token
    # print(BuyNowApi.buyer_token)
