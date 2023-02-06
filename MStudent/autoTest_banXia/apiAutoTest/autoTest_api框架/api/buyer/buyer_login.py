# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.buyer.base_buyer import BaseBuyerApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class BuyerLoginApi(BaseBuyerApi):
    """
    类实例化一定不能放在init构造方法中，否则会形成递归，造成会导致递归超过最大深度(1000)或内存泄漏等情况

    param = {'username': "mtx0327", 'password': "fcea920f7412b5da7be0cf42b8c93759", 'captcha': "1512",
             'uuid': "f6597380-4e24-11ed-984b-167610639c7"}
    method = "post"
    path = "/passport/login"

    """

    def __init__(self):  # path, method, params
        # 通过ini配置文件处理本接口的入参
        self.USERNAME = conf_parser_obj.configParser(["buyer_login", "username_buyer_login"])
        self.PASSWORD = conf_parser_obj.configParser(["buyer_login", "password_buyer_login"])
        self.PATH = conf_parser_obj.configParser(["buyer_login", "path_buyer_login"])
        self.CAPTCHA = conf_parser_obj.configParser(["buyer_login", "captcha"])
        self.METHOD = conf_parser_obj.configParser(["buyer_login", "method_buyer_login"])
        self.UUID = conf_parser_obj.configParser(["buyer_login", "uuid_buyer_login"])
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.desc = '买家登录'  # 便于日志信息描述
        self.url = f"{self.host}" + f"{self.PATH}"
        self.method = self.METHOD
        self.params = {'username': self.USERNAME, 'password': self.PASSWORD, 'captcha': self.CAPTCHA,
                       'uuid': self.UUID}

        # 此处不可BuyerLoginApi()实例对象调用send，会导致递归超过最大深度(1000),所以要用BuyerLoginApi类名调用send
        # self.token = BuyerLoginApi.send(self)  # send可用@staticmethod装饰器装饰城静态方法，即普通函数这样就能用类名调用了,同时self需手动传递

        # self.uid_cm = BuyerLoginApi().send_cm()[0]  # 类实例化一定不能放在init构造方法中，会造成递归

    # @property  # 装饰成私有化实例属性，别的类无法通过调用获得返回值
    # def send_token(self):  # 调用方式 self.send_token
    #     """该方法的参数化移交给init构造方法了"""
    #     self.res = self.request(url=self.url, method=self.method, params=self.params)  #
    #     # return self.res.json().get("uid"), self.res.json().get("access_token")
    #     return self.res.json().get('access_token')
    #
    # @property  # 将方法变成实例属性  调用方法: self.send_uid, 即实例对象.send_uid
    # def send_uid_token(self):  # 加上装饰器后，就是实例属性
    #     self.res = self.request(url=self.url, method=self.method, params=self.params)
    #     return self.res.json().get("uid"), self.res.json().get("access_token")
    #
    # def send(self):  # 加上装饰器后，就是普通函数，调用时
    #     """该方法的参数化移交给init构造方法了"""
    #     res = self.request(url=self.url, method=self.method, params=self.params)  #
    #     # return self.res.json().get("uid"), self.res.json().get("access_token")
    #     return res

    # 该方法不适用于属性构造
    # @classmethod
    # def send_cm(cls):
    #     res = cls().request(url=cls().url, method=cls().method, params=cls().params)
    #     return res.json().get("uid"), res.json().get("access_token")


if __name__ == "__main__":
    b = BuyerLoginApi()
    print(b.url)
    pprint(b.request().json())