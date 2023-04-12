# -*- coding=utf-8 -*-
# @Time    : 2023/02/07 04:51
# @Author  : ╰☆H.俠ゞ
# =============================================================
from api.buyer.base_buyer import BaseBuyerApi


class RogApi(BaseBuyerApi):
    """买家确认收货"""

    def __init__(self, order_sn):
        super().__init__()
        self.url = f"{self.host}/trade/orders/{order_sn}/rog"
        self.method = 'post'
        self.desc = '买家确认收货'