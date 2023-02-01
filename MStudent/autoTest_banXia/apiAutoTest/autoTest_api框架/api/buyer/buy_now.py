# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 11:46
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests


class buyNowApi:  # 业务成功将订单信息存入redis

    def __init__(self):
        self.url = "http://www.mtxshop.com:7002/trade/carts/buy"
        self.method = "post"
        self.res = None
        self.header = {"Authorization": "token"}
        self.params = {
            "sku_id": 600,
            "num": 1
        }

    def send(self):
        session = requests.sessions.Session()
        self.res = session.request(url=self.url, method=self.method, params=self.params, headers=self.header)
        return self.res


