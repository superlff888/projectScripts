# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 14:23
# @Author  : ╰☆H.俠ゞ
# =============================================================
from common.file_load import get_yml
from common.httpReuquests import HttpRequestCookies


class BaseBuyerApi(HttpRequestCookies):
    """类属性接收token"""
    buyer_token = ''
    buyer_uid = ''

    def __init__(self):
        super().__init__()
        self.host = get_yml('/conf/http.yml').get("buyer")
        self.headers = {"Authorization": BaseBuyerApi.buyer_token}
        self.uid = BaseBuyerApi.buyer_uid


if __name__ == '__main__':
    print(BaseBuyerApi().host)
