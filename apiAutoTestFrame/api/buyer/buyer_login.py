# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
from api.buyer.base_buyer import BaseBuyerApi
from common.encry_and_decry import md5
from common.fileload import get_yml


class BuyerLoginApi(BaseBuyerApi):

    def __init__(self):
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        # 通过ini配置文件处理本接口的入参
        self.USERNAME = get_yml('/conf/common.yml').get("buyerName")
        self.PASSWORD = get_yml('/conf/common.yml').get("buyerPassword")
        self.PATH = get_yml('/conf/common.yml').get("path_buyer_login")
        self.CAPTCHA = get_yml('/conf/common.yml').get("captcha")
        self.method = get_yml('/conf/common.yml').get("method_buyer_login")
        self.UUID = get_yml('/conf/common.yml').get("uuid_buyer_login")
        self.desc = '买家登录'  # 便于日志信息描述
        self.url = f"{self.host}" + f"{self.PATH}"
        self.params = {'username': self.USERNAME, 'password': md5(self.PASSWORD), 'captcha': self.CAPTCHA,
                       'uuid': self.UUID}
