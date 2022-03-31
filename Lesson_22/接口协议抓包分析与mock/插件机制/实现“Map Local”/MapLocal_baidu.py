# -*- coding=utf-8 -*-
# @Time    : 2022/03/31 20:45
# @Author  : ╰☆H.俠ゞ
# =============================================================


from mitmproxy import http


def request(flow: http.HTTPFlow):
    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.make(
            200,
            b"hello,world",
            {"Content-Type": "text/html"}
        )

