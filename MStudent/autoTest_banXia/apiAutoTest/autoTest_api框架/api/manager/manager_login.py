# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 17:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.manager.base_manager import BaseManagerApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class ManagerLoginApi(BaseManagerApi):

    def __init__(self):  # path, method, params
        self.USERNAME = conf_parser_obj.configParser(["manager_login", "username"])
        self.PASSWORD = conf_parser_obj.configParser(["manager_login", "password"])
        self.PATH = conf_parser_obj.configParser(["manager_login", "path_login"])
        self.CAPTCHA = conf_parser_obj.configParser(["manager_login", "captcha"])
        self.METHOD = conf_parser_obj.configParser(["manager_login", "method_login"])
        self.uuid = conf_parser_obj.configParser(["manager_login", "uuid"])
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.desc = '管理员登录'  # 便于日志信息描述
        self.url = f"{self.host}" + f"{self.PATH}"
        self.method = self.METHOD
        self.params = {'username': self.USERNAME, 'password': self.PASSWORD, 'captcha': self.CAPTCHA,
                       'uuid': self.uuid}


if __name__ == "__main__":
    b = ManagerLoginApi()
    pprint(b.request().json()['access_token'])