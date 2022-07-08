# -*- coding=utf-8 -*-
# @Time    : 2022/07/08 21:04
# @Author  : ╰☆H.俠ゞ
# =============================================================

#  加密

import base64
import hashlib
import json
import requests

string = "180vfdvuhkgb"

a = base64.b64encode(string.encode())  # encode二进制字节码编码
print(a)

b = base64.b64decode(a).decode()  # decode解码成字符串

print(b)


class Base64:

    def b64en(self, strings):
        # 加密
        base64.b64encode(strings.encode())  # encode二进制字节码编码

    def b64de(self, byte):
        # 解密
        base64.b64decode(byte).decode()  # decode解码成字符串


class ApiRequest:

    """
    # 参数举例：
    req_data = {
            "method": "get",
            "url": "127.0.0.1:9999/demo.txt",  # cmd本地启动web服务 python -m http.server 9999
            "header": None,
            "encoding": "base64"
        }"""

    def send(self, data: dict, url):
        """
        响应值解密
        """
        res = requests.request(data["method"], data["url"], headers=data["header"])
        if data["encoding"] == "base64":
            json.loads(base64.b64decode(res.content))

        # 加密后的响应值发给第三方服务，让第三方解密然后再返回
        elif data["encoding"] == "private":  # private 虚拟其他解密方式

            return requests.post(url, data=res.content)

