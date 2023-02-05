# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 00:51
# @Author  : ╰☆H.俠ゞ
# =============================================================
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.httpReuquests import HttpRequestCookies
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class BaseManagerApi(HttpRequestCookies):
    """
    不需要经过中间类BaseBuyerApi从登录类BuyerLoginApi中获取uid和token.
    因此，该类后期不做维护……
    """
    manager_token = ''

    def __init__(self):
        super().__init__()
        self.host = conf_parser_obj.configParser(["base_manager", "host"])
        self.headers = {"Authorization": BaseManagerApi.manager_token}


if __name__ == '__main__':
    print(BaseManagerApi().host)
