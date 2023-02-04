# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 21:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os

import javaobj
import pytest

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buy_now import BuyNowApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.common.excel_loading import read_data


class TestBuyNow:

    """
    ../reports/shop  测试用例包下py文件的相对路径


    [pytest
        addopts = -sv
                  --alluredir ../reports/shop --clean-alluredir
    """

    data, case_name = read_data()  # 解包：数据，用例标题

    @pytest.mark.parametrize("sku_id, num, except_code", data, ids=case_name)
    def test_buy_now(self, sku_id: int, num: int, except_code, got_resConn):
        """BuyNowApi子类从BuyerLoginApi父类构造方法中间接继承了实例属性uid  super().__init__()"""
        # buyer_login_api = BuyerLoginApi()
        # res = buyer_login_api.send(buyer_login_api)
        # print(f"\n登录接口响应:uid = {res[0]}, token = {res[1]}")
        # uid = res[0]

        buy_now_api = BuyNowApi(sku_id, num)
        uid = buy_now_api.uid  # 父类属性通过继承父类__init__构造方法,简介继承父类实例属性
        p_sku_id = buy_now_api.params.get("sku_id")
        p_num = buy_now_api.params.get("num")
        res = buy_now_api.send()
        code = res.status_code
        # redis
        bContent = got_resConn.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_' + str(uid))  # 强转为字符换，然后字符转拼接
        # 从redis缓存中将Java序列化Value转换为二进制(bytes)python对象
        resList = javaobj.loads(bContent)
        obj = resList[0]  # java对象
        # print(obj)  # 打印java对象
        # print(dir(obj))  # dir(obj)返回参数(java对象)的属性、方法列表
        skuId = obj.__getattribute__("skuId")
        num = obj.__getattribute__("num")
        # 断言
        pytest.assume(code == except_code)
        pytest.assume(skuId == p_sku_id)
        pytest.assume(num == p_num)
