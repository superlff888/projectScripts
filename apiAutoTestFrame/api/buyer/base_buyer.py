# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 14:23
# @Author  : ╰☆H.俠ゞ
# =============================================================
from common.fileload import get_yml
from common.httpclient import HttpClient


class BaseBuyerApi(HttpClient):
    BUYER_TOKEN = ''
    BUYER_UID = ''

    def __init__(self):
        super().__init__()
        self.host = get_yml("con/http.yml").get("buyer")
        self.headers = {"Authorization": BaseBuyerApi.BUYER_TOKEN}
        self.uid = BaseBuyerApi.BUYER_UID