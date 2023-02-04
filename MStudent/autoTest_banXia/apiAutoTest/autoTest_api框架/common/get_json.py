# -*- coding=utf-8 -*-
# @Time    : 2023/02/04 14:46
# @Author  : ╰☆H.俠ゞ
# =============================================================

import json

from autoTest_banXia.apiAutoTest.autoTest_api框架.setting import DIR_NAME


def get_json(path):
    """path为文件数据的绝对路径"""
    try:
        with open(DIR_NAME+path) as f:
            data = f.read()
            json_data = json.loads(data)
            return json_data
    except Exception as e:
        raise e


print(get_json("../data/a.json"))