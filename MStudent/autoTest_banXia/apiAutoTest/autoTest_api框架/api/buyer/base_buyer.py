# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 14:23
# @Author  : ╰☆H.俠ゞ
# =============================================================
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.httpReuquests import HttpRequestCookies
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class BaseBuyerApi(HttpRequestCookies):
    """
    不需要经过中间类BaseBuyerApi从登录类BuyerLoginApi中获取uid和token.
    因此，该类后期不做维护……
    """
    buyer_token = ''
    buyer_uid = ''

    def __init__(self):
        super().__init__()
        self.host = conf_parser_obj.configParser(["base_buyer", "host"])
        self.headers = {"Authorization": BaseBuyerApi.buyer_token}
        self.uid = BaseBuyerApi.buyer_uid
