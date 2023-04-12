# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 22:33
# @Author  : ╰☆H.俠ゞ
# =============================================================


class Singleton:

    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance