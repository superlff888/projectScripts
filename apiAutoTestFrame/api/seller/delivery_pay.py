# -*- coding=utf-8 -*-
# @Time    : 2023/02/07 04:30
# @Author  : ╰☆H.俠ゞ
# =============================================================
from api.seller.base_seller import BaseSellerApi


class DeliveryApi(BaseSellerApi):
    """卖家发货"""

    # 交易单号 动态传参
    def __init__(self, order_sn):
        super().__init__()
        self.url = f"{self.host}/seller/trade/orders/{order_sn}delivery"
        self.method = 'post'
        self.data = {"ship_no": "007", "logi_id": 13, "logi_name": "%E4%B8%AD%E9%80%9A01"}


class PayApi(BaseSellerApi):
    """卖家确认收款"""

    # 商品、价格 动态传参
    def __init__(self, order_sn, price):
        super().__init__()
        self.url = f"{self.host}/seller/trade/orders/{order_sn}/pay"
        self.method = 'post'
        self.data = {"pay_price": price}