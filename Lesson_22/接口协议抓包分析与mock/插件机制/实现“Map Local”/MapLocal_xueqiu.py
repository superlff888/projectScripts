# -*- coding=utf-8 -*-
# @Time    : 2022/03/31 23:50
# @Author  : ╰☆H.俠ゞ
# =============================================================

from mitmproxy import http


def request(flow: http.HTTPFlow):
    if "quote.json" in flow.request.pretty_url:
        # 打开本地数据文件
        with open(r"C:\Users\HouseLee\Desktop\maplocal.json") as f:
            flow.response = http.Response.make(
                200,
                f.read(),  # 读取本地文件中的数据作为响应内容
                {"Content-Type": "application/json",
                 "myHeader": "lee"}
            )