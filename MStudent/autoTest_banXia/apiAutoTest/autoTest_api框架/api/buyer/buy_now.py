# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 11:46
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

import requests
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.base_buyer import BaseBuyerApi


# 可递归继承“爷爷”辈的类方法(含init方法)和类属性 HttpRequestCookies
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buyer_login import BuyerLoginApi


class BuyNowApi(BuyerLoginApi):  # 业务成功将订单信息存入redis

    def __init__(self, sku_id, num):
        # 间接继承父类的header  super().__init__() ；把父类的属性拿来为我所用，可以直接用，也可重新复制
        # 【继承】可以继承父类的类属性和方法(包括__init__构造方法)，但不能直接继承实例属性；同BuyerLoginApi().__init__()
        super().__init__()
        self.header = {"Authorization": self.token}  # super().__init__() 已经拿到了header属性，不需要重复写
        self.url = f"{self.host}/trade/carts/buy"
        self.method = "post"
        self.res = None
        # 重写赋值父类的实例属性params
        self.params = {
            "sku_id": sku_id,
            "num": num
        }

    # 立即购买接口没有响应体内容
    def send(self):
        self.res = self.request(url=self.url, method=self.method, params=self.params, headers=self.header_pro)
        return self.res


if __name__ == '__main__':
    buyer_login_api = BuyerLoginApi()
    res = buyer_login_api.send(buyer_login_api)
    print(f"\n登录接口响应:uid = {res[0]}, token = {res[1]}")
    buy_now_api = BuyNowApi(600, 1)
    print(f"BuyNowApi请求头header_pro： {buy_now_api.header_pro}")
    print(BuyNowApi(600, 1).send().status_code)

