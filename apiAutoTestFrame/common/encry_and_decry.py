# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 22:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
import hashlib


def md5(data):

    return hashlib.md5(data.encode(encodings="utf-8")).hexdigest()