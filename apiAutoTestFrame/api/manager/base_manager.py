# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 00:51
# @Author  : ╰☆H.俠ゞ
# =============================================================
from common.file_load import get_yml
from common.httpReuquests import HttpRequestCookies


class BaseManagerApi(HttpRequestCookies):
    """
    不需要经过中间类BaseBuyerApi从登录类BuyerLoginApi中获取uid和token.
    因此，该类后期不做维护……
    """
    manager_token = ''

    def __init__(self):
        super().__init__()
        self.host = get_yml('/conf/http.yml').get("manager")
        self.headers = {"Authorization": BaseManagerApi.manager_token}


if __name__ == '__main__':
    print(BaseManagerApi().host)
