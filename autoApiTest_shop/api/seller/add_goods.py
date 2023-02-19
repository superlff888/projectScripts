# -*- coding=utf-8 -*-
# @Time    : 2023/02/04 10:32
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from api.seller.base_seller import BaseSellerApi
from api.seller.seller_login import SellerLoginApi
from common.file_load import get_json


class AddGoodsApi(BaseSellerApi):
    """添加商品"""

    def __init__(self):
        super().__init__()
        self.desc = '卖家添加商品'
        self.url = f'{self.host}' + "/seller/goods"
        self.method = 'post'
        self.json = get_json("/data/goods_seller.json")


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
