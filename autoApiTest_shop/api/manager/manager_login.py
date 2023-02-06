# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 17:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
from api.manager.base_manager import BaseManagerApi
from common.file_load import conf_parser_obj


class ManagerLoginApi(BaseManagerApi):

    def __init__(self):
        self.USERNAME = conf_parser_obj.configParser(["manager_login", "username_manager_login"])
        self.PASSWORD = conf_parser_obj.configParser(["manager_login", "password_manager_login"])
        self.PATH = conf_parser_obj.configParser(["manager_login", "path_manager_login"])
        self.CAPTCHA = conf_parser_obj.configParser(["manager_login", "captcha"])
        self.METHOD = conf_parser_obj.configParser(["manager_login", "method_manager_login"])
        self.uuid = conf_parser_obj.configParser(["manager_login", "uuid_manager_login"])
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.desc = '管理员登录'  # 便于日志信息描述
        self.url = f"{self.host}" + f"{self.PATH}"
        self.method = self.METHOD
        self.params = {'username': self.USERNAME, 'password': self.PASSWORD, 'captcha': self.CAPTCHA,
                       'uuid': self.uuid}


if __name__ == "__main__":
    b = ManagerLoginApi()
    # pprint(f"管理员登录接口token: {b.request().json()['access_token']}")
    print(f"管理员登录接口token: {b.request().json()['access_token']}")