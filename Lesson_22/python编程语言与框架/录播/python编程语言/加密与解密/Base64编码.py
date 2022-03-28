# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 10:14
# @Author  : ╰☆H.俠ゞ
# =============================================================

import base64
import json

import requests

string = '你好啊'
# 编码： 字符串 -> 二进制 -> base64编码
b64_code = base64.b64encode(string.encode())
print(b64_code)  # b'5L2g5aW95ZWK'

url1 = 'https://httpbin.testing-studio.com/get'
r = requests.get('https://httpbin.testing-studio.com/get')
print(r.content)
b64 = base64.b64encode(r.content)
print(b64)  # b64encode需传递二进制参数对对象


# 解码：base64编码 -> 二进制 -> 字符串
port_str = base64.b64decode(b64_code).decode()
print(port_str)  # '你好啊'

url2 = 'https://httpbin.testing-studio.com/get'
r = requests.get('https://httpbin.testing-studio.com/get')
res = json.loads(base64.b64decode(b64))  # python 字典dict
res2 = base64.b64decode(b64)  # json二进制
print(res)
print(type(res))  # python 字典dict
print(res2)
print(type(res2))   # json二进制

