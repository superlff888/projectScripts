# -*- coding=utf-8 -*-
# @Time    : 2023/02/03 10:00
# @Author  : ╰☆H.俠ゞ
# =============================================================
from autoTest_banXia.apiAutoTest.autoTest_api框架.common.httpReuquests import HttpRequestCookies


class BaseSellerApi(HttpRequestCookies):
    seller_token = ''

    def __init__(self):
        super().__init__()
        self.host = 'http://www.mtxshop.com:7003'
        self.header = {"Authorization": BaseSellerApi.seller_token}