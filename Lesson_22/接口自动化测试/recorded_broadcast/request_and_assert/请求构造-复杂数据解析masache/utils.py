# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 14:13
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json


def read_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        create_emp = json.load(f)
    return create_emp
