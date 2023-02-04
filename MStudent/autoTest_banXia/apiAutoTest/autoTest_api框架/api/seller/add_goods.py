# -*- coding=utf-8 -*-
# @Time    : 2023/02/04 10:32
# @Author  : ╰☆H.俠ゞ
# =============================================================
from autoTest_banXia.apiAutoTest.autoTest_api框架.api.seller.base_seller import BaseSellerApi


class AddGoods(BaseSellerApi):

    def __init__(self):
        super().__init__()
        self.method = 'post'

