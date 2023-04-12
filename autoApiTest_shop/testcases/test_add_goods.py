# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 12:55
# @Author  : ╰☆H.俠ゞ
# =============================================================
import allure
import pytest
from api.seller.add_goods import AddGoodsApi


@pytest.mark.usefixtures("get_token")
@allure.feature("卖家接口")
class TestAddGoods:

    @allure.story("卖家添加商品接口")  # 功能点
    @allure.title("正常添加商品")  # 用例标题   allure报告中的title
    def test_add_goods(self):
        add_goods = AddGoodsApi()
        uid = add_goods.uid
        res = add_goods.request()
        code = res.status_code

        pytest.assume(code == 200)
        pytest.assume(uid == 61293)