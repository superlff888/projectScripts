# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 11:46
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

# 可递归继承“爷爷”辈的类方法(含init方法)和类属性 HttpRequestCookies
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.buyer_login import BuyerLoginApi
from autoTest_banXia.apiAutoTest.autoTest_api框架.common.logger import Logging
from autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class BuyNowApi(BuyerLoginApi):  # 业务成功将订单信息存入redis

    """类属性一般为常量，不经常发生变换，故适合维护在配置文件中"""
    PATH = conf_parser_obj.configParser(["buy_now", "path"])
    METHOD = conf_parser_obj.configParser(["buy_now", "method"])
    LEVEL = conf_parser_obj.configParser(["logging", "level"])
    PATH1 = conf_parser_obj.configParser(["logging", "filepath"])  # ini配置文件中options中key不能维护成path
    logger = Logging(LEVEL, PATH1)  # './logs/shopLog.log'

    def __init__(self, sku_id=600, num=1):
        # 间接继承父类的header  super().__init__() ；把父类的属性拿来为我所用，可以直接用，也可重新复制
        # 【继承】可以继承父类的类属性和方法(包括__init__构造方法)，但不能直接继承实例属性；同BuyerLoginApi().__init__()
        super().__init__()
        # 只能用父类实例对象调用property属性,@property装饰器保护机制，相当于父类的私有属性
        self.uid, self.token = BuyerLoginApi().send_uid_token  # 每个人间的token和uid都不相同，所以不可通过两次实例化获得uid和token
        self.header = {"Authorization": self.token}  # 子类无法直接调用property属性
        # self.header = {"Authorization": BuyerLoginApi.send(BuyerLoginApi())}  # 子类无法直接调用property属性
        self.url = f"{self.HOST}" + f"{self.PATH}"
        self.method = self.METHOD
        self.res = None
        # 重写赋值父类的实例属性params
        self.params = {
            "sku_id": sku_id,
            "num": num
        }

    # 立即购买接口没有响应体内容
    def send(self):
        """该方法的参数化移交给init构造方法了"""
        self.logger.info(f'正在发送请求...\n请求方法: {self.method},请求参数: {self.params}')
        self.res = self.request(url=self.url, method=self.method, params=self.params, headers=self.header)
        return self.res


if __name__ == '__main__':
    buy_now_api = BuyNowApi()  # sku_id=600, num=1
    print(f"BuyNowApi请求头header: {buy_now_api.uid}")
    # print(f"BuyNowApi请求头header: {buy_now_api.url}")
    # print(f"BuyNowApi请求头header: {buy_now_api.header}")
    print(f"BuyNowApi响应状态码: {buy_now_api.send()}")


