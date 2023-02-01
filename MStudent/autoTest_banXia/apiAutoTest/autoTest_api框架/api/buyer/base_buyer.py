# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 14:23
# @Author  : ╰☆H.俠ゞ
# =============================================================
from autoTest_banXia.apiAutoTest.autoTest_api框架.common.httpReuquests import HttpRequestCookies, HttpRequest


class BaseBuyerApi(HttpRequestCookies):

    buyer_token = ''

    def __init__(self):
        super().__init__()
        self.host = 'http://mtxshop.com:7002'
        self.header = {"Authorization": BaseBuyerApi.buyer_token}
