# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 21:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.base_buyer import BaseBuyerApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buy_now import BuyNowApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buyer_login import BuyerLoginApi


class TestBuyNow:

    def test_buy_now(self):
        res = BuyerLoginApi().send()
        token = res.json()["access_token"]
        BaseBuyerApi.buyer_token = token
        # print(BuyNowApi.buyer_token)
        buy_now_api = BuyNowApi()
        res = buy_now_api.send()
        code = res.status_code
        pytest.assume(code == 200)