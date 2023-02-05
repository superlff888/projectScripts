# -*- coding=utf-8 -*-
# @Time    : 2023/02/04 14:46
# @Author  : ╰☆H.俠ゞ
# =============================================================

import json

from autoTest_banXia.apiAutoTest.autoTest_api框架.setting import DIR_NAME


def get_json(path):
    """path为文件数据的绝对路径"""
    try:
        with open(DIR_NAME+path, encoding="utf-8") as f:
            data = f.read()
            json_data = json.loads(data)
            return json_data
    except Exception as e:
        raise e


if __name__ == '__main__':
    print(DIR_NAME)
    print(get_json("/data/goods_seller.json"))