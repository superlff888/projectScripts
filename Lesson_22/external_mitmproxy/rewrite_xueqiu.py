# -*- coding=utf-8 -*-
# @Time    : 2022/04/01 21:39
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json

from mitmproxy import http


def response(flow: http.HTTPFlow) -> None:
    print(flow.response.content)
    data = json.loads(flow.response.content)  # 转化为python对象
    print(data)