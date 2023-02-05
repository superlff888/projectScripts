# -*- coding=utf-8 -*-
# @Time    : 2023/02/04 10:32
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from autoTest_banXia.apiAutoTest.autoTest_api框架.api.seller.base_seller import BaseSellerApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.api.seller.seller_login import SellerLoginApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.common.get_json import get_json

class AddGoodsApi(BaseSellerApi):

    def __init__(self):
        super().__init__()
        self.url = f'{self.host}' + "/seller/goods"
        self.method = 'post'
        self.json = get_json("/data/goods_seller.json")

    # def send(self):  # 直接调用底层方法即可
    #     global goods_id
    #     goods_id = self.request(url=self.url, method=self.method, json=self.json, headers=self.headers).json()["goods_id"]
    #     return goods_id


if __name__ == '__main__':
    sl = SellerLoginApi()
    print(f"卖家登录url：{sl.url}")
    res = sl.request()  # 底层的方法
    token = res.json()["access_token"]
    uid = res.json()["uid"]
    BaseSellerApi.seller_token = token
    BaseSellerApi.seller_uid = uid

    add_goods = AddGoodsApi()
    print(add_goods.headers)
    res = add_goods.request()
    # pprint(res.json(), indent=2)
    pprint(res.status_code, indent=2)
