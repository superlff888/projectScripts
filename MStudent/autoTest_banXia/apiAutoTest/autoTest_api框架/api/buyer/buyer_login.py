# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from autoTest_banXia.apiAutoTest.autoTest_api框架.common.httpReuquests import HttpRequestCookies, HttpRequest


class BuyerLoginApi(HttpRequestCookies):

    def __init__(self):
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.host = 'http://www.mtxshop.com:7002'
        self.url = f'{self.host}' + "/passport/login"
        self.method = "post"
        self.params = dict(username="mtx0327", password="fcea920f7412b5da7be0cf42b8c93759", captcha="1512",
                           uuid="f6597380-4e24-11ed-984b-167610639c7")

        # 此处不可BuyerLoginApi()实例对象调用send，会导致递归超过最大深度(1000),所以要用BuyerLoginApi类名调用send
        self.uid = BuyerLoginApi.send(self)[0]  # send可用@staticmethod装饰器，这样就能用类名调用了
        self.token = BuyerLoginApi.send(self)[1]  # 支持实例对象调用静态方法，只是放在构造方法中，会出现递归情况
        self.header = {"Authorization": self.token}

        # self.uid_cm = BuyerLoginApi().send_cm()[0]  # 类实例化一定不能放在init构造方法中，会造成递归

    @staticmethod  # 将方法装饰城静态方法，即普通函数，使用类名调用该方法，同时self需手动传递
    def send(self):  # 加上装饰器后，就是普通函数，调用时
        self.res = self.request(url=self.url, method=self.method, params=self.params)
        return self.res.json().get("uid"), self.res.json().get("access_token")

    # @property  # 将方法变成实例属性
    # def sendPlus(self):  # 加上装饰器后，就是实例属性
    #     self.res = self.request(url=self.url, method=self.method, params=self.params)
    #     # return [self.res.json().get("uid"),  self.res.json().get("access_token")]
    #     return self.res.json()

    # @sendPlus.setter()
    # def sendPlus(self, value: str):
    #     value: str

    # @classmethod
    # def send_cm(cls):
    #     res = cls().request(url=cls().url, method=cls().method, params=cls().params)
    #     return res.json().get("uid"), res.json().get("access_token")


if __name__ == "__main__":
    b = BuyerLoginApi()
    print(b.send(b))
    print(type(b.send(b)))
