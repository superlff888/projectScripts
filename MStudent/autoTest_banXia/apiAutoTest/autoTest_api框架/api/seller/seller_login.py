# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from autoTest_banXia.apiAutoTest.autoTest_api框架.api.seller.base_seller import BaseSeller


class SellerLoginApi(BaseSeller):
    """
    类实例化一定不能放在init构造方法中，否则会形成递归，造成会导致递归超过最大深度(1000)或内存泄漏等情况
    """

    def __init__(self):
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.url = f'{self.host}' + "/seller/login"
        self.method = "post"
        self.params = dict(username="mtx0327", password="fcea920f7412b5da7be0cf42b8c93759", captcha="1512",
                           uuid="f6597380-4e24-11ed-984b-167610639c7")
