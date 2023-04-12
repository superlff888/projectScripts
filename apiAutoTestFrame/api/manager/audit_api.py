# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 17:40
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from api.manager.base_manager import BaseManagerApi
from api.manager.manager_login import ManagerLoginApi
from common.file_load import get_yml


class AuditApi(BaseManagerApi):

    def __init__(self, goods_id):  # [19812, 19815]
        super().__init__()
        self.desc = '商品审核'
        self.method = get_yml('/conf/common.yml').get("method_audit")
        self.path = get_yml('/conf/common.yml').get("path_audit")
        self.url = f"{self.host}" + f"{self.path}"
        self.json = {
                    "goods_ids": [goods_id],
                    "message": "审核通过20230205",
                    "pass": 1
                    }


if __name__ == '__main__':
    mla = ManagerLoginApi()
    res = mla.request()
    token = res.json()["access_token"]
    BaseManagerApi.manager_token = token
    aa = AuditApi([19812, 19815])
    pprint(f"header:{aa.headers}")
    # pprint(AuditApi().request().json())

