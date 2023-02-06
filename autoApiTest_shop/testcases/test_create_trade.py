# -*- coding=utf-8 -*-
# @Time    : 2023/02/06 13:31
# @Author  : ╰☆H.俠ゞ
# =============================================================
import allure
import pytest

from api.buyer.buy_now import BuyNowApi
from api.buyer.create_trade import BuyerTradeApi
from common.mysql_conn import DbConnect


@allure.feature("买家接口")
class TestTrade:

    @allure.story("创建交易接口")
    @allure.title("创建交易成功")
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
        # 查询数据库
        data = db.select(f"select member_id, member_name from es_order where trade_sn = {trade_sn}")
        memberId = data[0]["member_id"]
        memberName = data[0]["member_name"]
        # 断言 接口返回与数据库结果校验
        pytest.assume(member_id == memberId)
        pytest.assume(member_name == memberName)