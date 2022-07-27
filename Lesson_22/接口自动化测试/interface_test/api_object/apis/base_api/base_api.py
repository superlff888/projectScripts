# -*- coding=utf-8 -*-
# @Time    : 2022/07/27 21:01
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests
import urllib3

"""对底层框架的封装"""


class BaseApi:
    """对发送请求的接口测试工具进行封装"""
    def send_api(self, req, tools="requests"):  # 注意：此处不能用“**req”，调用request时才需要解包
        """
        :: param  tools 如果以后出现比requests更好用的库,可以替换掉requests
        :: param req  url、method、param、data、json
        """
        if tools == "requests":
            return requests.request(**req)
        if tools == "urllib3":
            pass