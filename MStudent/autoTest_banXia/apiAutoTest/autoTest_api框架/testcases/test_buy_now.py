# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 21:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
import javaobj
import pytest

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buy_now import BuyNowApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buyer_login import BuyerLoginApi


class TestBuyNow:

    """
    ../reports/shop  测试用例包下py文件的相对路径


    [pytest]
        addopts = -sv
                  --alluredir ../reports/shop --clean-alluredir
    """

    def test_buy_now(self, got_resConn):
        """BuyNowApi子类从BuyerLoginApi父类构造方法中间接继承了实例属性uid  super().__init__()"""
        # buyer_login_api = BuyerLoginApi()
        # res = buyer_login_api.send(buyer_login_api)
        # print(f"\n登录接口响应:uid = {res[0]}, token = {res[1]}")
        # uid = res[0]

        buy_now_api = BuyNowApi()
        uid = buy_now_api.uid  # 父类属性通过继承父类__init__构造方法,简介继承父类实例属性
        res = buy_now_api.send()
        code = res.status_code

        p_sku_id = buy_now_api.params.get("sku_id")
        p_num = buy_now_api.params.get("num")

        bContent = got_resConn.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_' + str(uid))  # 强转为字符换，然后字符转拼接
        # 从redis缓存中将Java序列化Value转换为二进制(bytes)python对象
        resList = javaobj.loads(bContent)
        obj = resList[0]  # java对象
        # print(obj)  # 打印java对象
        # print(dir(obj))  # dir(obj)返回参数(java对象)的属性、方法列表
        skuId = obj.__getattribute__("skuId")
        num = obj.__getattribute__("num")
        # print(skuId)  # 获取'skuId'属性值
        # print(num)  # 获取'num'属性值

        pytest.assume(code == 200)
        pytest.assume(skuId == p_sku_id)
        pytest.assume(num == p_num)
