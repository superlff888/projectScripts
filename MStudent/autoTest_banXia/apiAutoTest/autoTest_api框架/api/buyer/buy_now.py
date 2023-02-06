# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 11:46
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

# 可递归继承“爷爷”辈的类方法(含init方法)和类属性 HttpRequestCookies
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.base_buyer import BaseBuyerApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buyer_login import BuyerLoginApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class BuyNowApi(BaseBuyerApi):  # 业务成功将订单信息存入redis

    def __init__(self, sku_id=600, num=1):
        """类属性一般为常量，不经常发生变换，故适合维护在配置文件中"""
        self.PATH = conf_parser_obj.configParser(["buy_now", "path_buy"])
        self.METHOD = conf_parser_obj.configParser(["buy_now", "method_buy"])
        # 间接继承父类的header  super().__init__() ；把父类的属性拿来为我所用，可以直接用，也可重新复制
        # 【继承】可以继承父类的类属性和方法(包括__init__构造方法)，但不能直接继承实例属性；同BuyerLoginApi().__init__()
        super().__init__()
        self.desc = '立即购买'
        self.url = f"{self.host}" + f"{self.PATH}"
        self.method = self.METHOD
        self.res = None
        # 重写赋值父类的实例属性params
        self.params = {
            "sku_id": sku_id,
            "num": num
        }

    # 立即购买接口没有响应体内容
    # def send(self):
    #     """该方法的参数化移交给init构造方法了"""
    #     # self.logger.info(f'正在发送请求...\n请求方法: {self.method},请求参数: {self.params}')
    #     self.res = self.request(url=self.url, method=self.method, params=self.params, headers=self.header)
    #     return self.res


if __name__ == '__main__':
    bl = BuyerLoginApi()
    print(f"买家登录接口url为: {bl.url}")
    res = bl.request()
    token = res.json()["access_token"]
    uid = res.json()["uid"]
    print(f"买家登录接口返回的token为: {token}")
    # BaseBuyerApi.buyer_token = token
    # BaseBuyerApi.buyer_uid = uid
    # buy_now_api = BuyNowApi()  # sku_id=600, num=1
    # print(f"立即购买请求url: {buy_now_api.url}")
    # print(f"BuyNowApi请求method: {buy_now_api.method}")
    # print(f"BuyNowApi请求header: {buy_now_api.headers}")
    # print(f"BuyNowApi请求params: {buy_now_api.params}")
    # print(f"BuyNowApi响应状态码: {buy_now_api.request().status_code}")


