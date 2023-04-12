# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 12:55
# @Author  : ╰☆H.俠ゞ
# =============================================================

import allure
import javaobj
import pytest

from api.buyer.buy_now import BuyNowApi
from common.file_load import getCSV, get_excel


@pytest.mark.usefixtures("get_token")
@allure.feature("买家接口")  # 模块
class TestBuyNow:
    """尽量使用excel，后面可用不同sheet页维护多种数据"""

    filepath = r'/data/shop_data.xlsx'
    sheet_name = '立即购买'
    data = get_excel(filepath, sheet_name)

    # filepath = r'/data/shop_data.csv'
    # data = getCSV(filepath)

    @allure.title("{case_name}")  # 用例标题   allure报告中的title
    @allure.story("买家立即购买接口")  # 功能点
    @pytest.mark.parametrize("case_name,sku_id, num, except_code", data)
    def test_buy_now_code(self, case_name, sku_id, num, except_code, Initialize_a_new_Redis_client):
        """BuyNowApi子类从BaseBuyerApi父类构造方法中间接继承了实例属性uid  super().__init__()"""

        buy_now_api = BuyNowApi(sku_id, num)
        res = buy_now_api.request()
        code = res.status_code
        # 断言
        pytest.assume(code == except_code)

    @allure.title("正常购买")
    def test_buy_now_ok(self, Initialize_a_new_Redis_client):
        """BuyNowApi子类从BaseBuyerApi父类构造方法中间接继承了实例属性uid  super().__init__()"""

        buy_now_api = BuyNowApi(sku_id=20105, num=1)
        uid = buy_now_api.uid  # 父类属性通过继承父类__init__构造方法,简介继承父类实例属性
        print(uid)
        p_sku_id = buy_now_api.params.get("sku_id")
        p_num = buy_now_api.params.get("num")
        res = buy_now_api.request()
        code = res.status_code

        # redis
        bContent = Initialize_a_new_Redis_client.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_' + str(uid))  # 强转为字符换，然后字符转拼接
        # print(f"bContent: {bContent}")
        # 从redis缓存中将Java序列化Value转换为二进制(bytes)python对象
        resList = javaobj.loads(bContent)
        obj = resList[0]  # python的"java类"的对象
        print(f"resList: {resList}")
        print(f"obj对象类属性和方法列表: {dir(obj)}")  # dir(obj)返回参数(java对象)的类属性、方法列表
        skuId = obj.__getattribute__("skuId")  # 获取属性值
        num = obj.__getattribute__("num")  # 获取属性值

        # 断言
        pytest.assume(code == 200)
        pytest.assume(skuId == p_sku_id)  # 入参跟redis缓存中的数据对比
        pytest.assume(num == p_num)

    @allure.story("测试功能点")
    @allure.severity(severity_level=allure.severity_level.BLOCKER)
    def test_demo(self):
        assert True

    @allure.story("测试功能点")
    @allure.severity("critical")
    def test_demo1(self):
        assert True

    @allure.story("功能点")
    @allure.severity("normal")
    def test_demo2(self):
        assert True

    @allure.story("测试功能点")
    @allure.severity("block")
    def test_demo3(self):
        assert True

    @allure.story("功能点")
    @allure.severity(allure.severity_level.MINOR)
    def test_demo4(self):
        assert True

    @allure.story("测试功能点")
    @allure.severity(allure.severity_level.TRIVIAL)
    def test_demo5(self):
        assert True