# -*- coding=utf-8 -*-
# @Time    : 2023/02/06 13:31
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buy_now import BuyNowApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.create_trade import BuyerTradeApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.mysql_conn import DbConnect


class TestTrade:

    @pytest.mark.usefixtures('get_token')  # 建议无返回值的fixture采用该方式调用
    def test_trade(self, db: DbConnect):  # 加上注解后，就可以联想出类中的方法和属性
        # 立即购买
        res = BuyNowApi().request()
        print(res.text)
        # 创建交易
        res = BuyerTradeApi().request()
        trade_sn = res.json()["trade_sn"]
        member_id = res.json()["member_id"]
        member_name = res.json()["member_name"]

        db.select(f"select member_id, member_name from es_order where trade_sn = {trade_sn}")