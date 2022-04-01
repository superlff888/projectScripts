# -*- coding=utf-8 -*-
# @Time    : 2022/03/31 20:45
# @Author  : ╰☆H.俠ゞ
# =============================================================


from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if "https://www.baidu.com" in flow.request.pretty_url:
        print("..............")
        flow.response = http.Response.make(
            200,  # (optional) status code
            b"Hello World",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )