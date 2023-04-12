# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 17:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from api.manager.base_manager import BaseManagerApi
from common.encry_decry import md5
from common.file_load import get_yml


class ManagerLoginApi(BaseManagerApi):

    def __init__(self):
        self.USERNAME = get_yml('/conf/common.yml').get("managerName")
        self.PASSWORD = get_yml('/conf/common.yml').get("managerPassword")
        self.PATH = get_yml('/conf/common.yml').get("path_manager_login")
        self.CAPTCHA = get_yml('/conf/common.yml').get("captcha")
        self.METHOD = get_yml('/conf/common.yml').get("method_manager_login")
        self.uuid = get_yml('/conf/common.yml').get("uuid_manager_login")
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.desc = '管理员登录'  # 便于日志信息描述
        self.url = f"{self.host}" + f"{self.PATH}"
        self.method = self.METHOD
        self.params = {'username': self.USERNAME, 'password': md5(self.PASSWORD), 'captcha': self.CAPTCHA,
                       'uuid': self.uuid}


if __name__ == "__main__":
    b = ManagerLoginApi()
    pprint(f"管理员登录接口token: {b.request().json()['access_token']}")
    # print(f"管理员登录接口token: {b.request().json()['access_token']}")