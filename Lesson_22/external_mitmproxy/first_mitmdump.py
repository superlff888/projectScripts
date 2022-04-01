
# -*- coding=utf-8 -*-
# @Time    : 2022/03/31 10:40
# @Author  : ╰☆H.俠ゞ
# =============================================================
from mitmproxy import http


# request方法名不能更改~hook
def request(flow: http.HTTPFlow):  # flow为mitmdump抓到的包
    flow.request.headers["myHeader"] = "lee"  # 添加或修改请求头信息
    print(flow.request.headers)
