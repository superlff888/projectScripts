# -*- coding=utf-8 -*-
# @Time    : 2022/03/31 20:45
# @Author  : ╰☆H.俠ゞ
# =============================================================


from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://www.baidu.com":
        flow.response = http.Response.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )