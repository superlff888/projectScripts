# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 11:07
# @Author  : ╰☆H.俠ゞ
# =============================================================

import requests
"""
r.text = r.encoding+r.content
r.json() = r.encoding+r.content+content type json


【form请求 参数data】
"Content-Type": "application/x-www-form-urlencoded"
【json请求 参数json】
"Content-Type": "application/json"
"""


class Test_demo:
    # get请求 默认params入参 带参数
    def test_get_demo(self):
        payload = {"level": 1, "name": "seveniruby"}
        r = requests.get("https://httpbin.testing-studio.com/get", payload)
        print(r.text)

    # get请求 params入参 带参数
    def test_get_param(self):
        payload = {"level": 1, "name": "seveniruby"}
        r = requests.get("https://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        print(r.json())
        print(r.request.method)

    # post请求 data传参=form表单 dict词典格式
    def test_post_form(self):

        """form表单形式传参  Content-Type:application/x-www-form-urlencoded"""

        data_payload = {"level": 1, "name": "seveniruby"}
        r = requests.post("https://httpbin.testing-studio.com/post", data=data_payload)
        print(r.text)

    # post请求 json（结构化）传参
    def test_post_json(self):
        payload = {"level": 1, "name": "seveniruby"}
        r = requests.post("https://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        print(r.cookies)
        assert r.json()['json']['level'] == 1

    # 文件上传 （仅模拟，无法执行）
    def test_post_file(self):
        file = {"file": open("report.xls", 'rb')}
        r = requests.post("https://httpbin.testing-studio.com/post", files=file)
        print(r.text)
        print(r.cookies)

    # header 附加到请求headers中
    def test_get_header(self):
        headers = {'H': 'HEADER_DEMO',
                   "User-Agent": "python-requests/2.25.8"}  # 覆盖或追加header信息
        r = requests.get("https://httpbin.testing-studio.com/get", headers=headers)  # 当人也可以post
        print(r.text)
        print(r.json()['headers']['H'])

    # cookies 通过cookies参数传递
    def test_get_cookies(self):
        cookies = dict(cookies_are='working', teacher='AD')  # 需要传递字典参数 {'cookies_are': 'working'};可传递多个cookie
        print(cookies)
        r = requests.get("https://httpbin.testing-studio.com/get", cookies=cookies)  # 也可post
        print(r.text)

    # Cookie 通过headers进行传递
    def test_get_Cookie(self):
        headers = {'Cookie': 'Cookie_Demo',
                   "User-Agent": "python-requests/2.25.8"}  # 覆盖或追加header信息
        r = requests.get("https://httpbin.testing-studio.com/get", headers=headers)  # 也可post
        print(r.text)

    # xml请求
    def test_post_xml(self):
        xml = """<?xml version='1.0' encoding='utf-8'?><a>6</a>"""
        headers = {'Content-Type': 'application/xml'}  # requests里没有封装xml，需要在headers里要追加application/xml
        r = requests.post('https://httpbin.testing-studio.com/post', data=xml, headers=headers)
        print(r.text)

