# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.seller.base_seller import BaseSellerApi


class SellerLoginApi(BaseSellerApi):
    """
    类实例化一定不能放在init构造方法中，否则会形成递归，造成会导致递归超过最大深度(1000)或内存泄漏等情况
    """

    def __init__(self):
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.url = f"{self.host}" + "/seller/login"
        self.method = "get"
        self.params = {'username': 'leeseller', 'password': 'e10adc3949ba59abbe56e057f20f883e', 'captcha': 1512,
                       'uuid': 'b281d2e0-a2e0-11ed-8996-69acd4b6dd14'}


if __name__ == '__main__':
    s = SellerLoginApi()
    res = s.request()  # 调用的底层httpRequestCookies方法
    pprint(res.json())