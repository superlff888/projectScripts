# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 半夏 微信：testfankevin
# @Time: 2022-11-20 10:13
# @Copyright：北京码同学
import allure
import pytest

from api.manager.audit_api import AuditApi
from api.seller.add_goods import AddGoodsApi

@allure.feature("管理员接口")
class TestAuditGoods:

    @allure.story("商品审核")
    @allure.title("商品审核")
    def test_audit(self):
        """
        提取token统一放在fixture

        业务分析：商品审核需要商品id --> 商品的id通过卖家的发布商品接口获取

        """

        # 发布商品
        add_api = AddGoodsApi()
        resp = add_api.request()
        # 提取goods_id
        good_id = resp.json()['goods_id']
        # 商品审核
        audit = AuditApi(goods_id=good_id)
        resp = audit.request()
        # print(resp.status_code)
        # print(resp.text)  # 审核商品通过后 响应体数据为空,直接使用json会报错
        # 断言响应状态码  200
        pytest.assume(resp.status_code == 200)
