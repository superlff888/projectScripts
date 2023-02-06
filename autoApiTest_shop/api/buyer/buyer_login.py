# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from api.buyer.base_buyer import BaseBuyerApi
from common.encry_decry import md5
from common.file_load import conf_parser_obj


class BuyerLoginApi(BaseBuyerApi):
    """
    类实例化一定不能放在init构造方法中，否则会形成递归，造成会导致递归超过最大深度(1000)或内存泄漏等情况

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
        self.params = {'username': self.USERNAME, 'password': md5(self.PASSWORD), 'captcha': self.CAPTCHA,
                       'uuid': self.UUID}


if __name__ == "__main__":
    b = BuyerLoginApi()
    pprint(b.request().json())