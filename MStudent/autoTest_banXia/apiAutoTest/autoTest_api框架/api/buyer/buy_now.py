# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 11:46
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

import requests

from autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.base_buyer import BaseBuyerApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buyer_login import BuyerLoginApi

# 可递归继承“爷爷”辈的类方法(含init方法)和类属性 HttpRequestCookies
class BuyNowApi(BaseBuyerApi):  # 业务成功将订单信息存入redis

    def __init__(self):
        # 把父类的属性拿来为我所用，可以直接用，也可重新复制
        # 继承父类的header
        super().__init__()  # 【继承】可以继承父类的类属性和方法(包括__init__构造方法)，但不能直接继承实例属性； 同BaseBuyerApi().__init__()
        self.url = f"{self.host}/trade/carts/buy"
        self.method = "post"
        self.res = None
        # self.header = {"Authorization": self.buyer_token}  # super().__init__() 已经拿到了header属性，不需要重复写
        self.params = {
            "sku_id": 600,
            "num": 1
        }

    def send(self):
        self.res = self.request(url=self.url, method=self.method, params=self.params, headers=self.header)
        return self.res


if __name__ == '__main__':
    res = BuyerLoginApi().send()
    token = res.json()["access_token"]
    BaseBuyerApi.buyer_token = token

