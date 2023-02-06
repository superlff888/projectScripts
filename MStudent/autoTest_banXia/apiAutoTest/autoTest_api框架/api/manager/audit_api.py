# -*- coding=utf-8 -*-
# @Time    : 2023/02/05 17:40
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.manager.base_manager import BaseManagerApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.api.manager.manager_login import ManagerLoginApi
from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class AuditApi(BaseManagerApi):

    def __init__(self):
        super().__init__()
        self.desc = '商品审核'
        self.method = conf_parser_obj.configParser(["audit", "method_audit"])
        self.path = conf_parser_obj.configParser(["audit", "path_audit"])
        self.url = f"{self.host}" + f"{self.path}"
        self.json = {
                    "goods_ids": [19812, 19815],
                    "message": "审核通过20230205",
                    "pass": 1
                    }


if __name__ == '__main__':
    mla = ManagerLoginApi()
    res = mla.request()
    token = res.json()["access_token"]
    BaseManagerApi.manager_token = token
    aa = AuditApi()
    pprint(aa.headers)
    # pprint(AuditApi().request().json())

