# -*- coding=utf-8 -*-
# @Time    : 2022/07/29 21:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
import jsonpath


class Jsonpath:
    @classmethod
    def myJsonpath(cls, obj, exp):
        return jsonpath.jsonpath(obj, exp)