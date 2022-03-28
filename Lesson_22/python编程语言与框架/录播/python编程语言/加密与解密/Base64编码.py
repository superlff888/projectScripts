# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 10:14
# @Author  : ╰☆H.俠ゞ
# =============================================================

import base64

string = '你好啊'
# 编码： 字符串 -> 二进制 -> base64编码
b64_code = base64.b64encode(string.encode())
print(b64_code)  # b'5L2g5aW95ZWK'


# 解码：base64编码 -> 二进制 -> 字符串
port_str = base64.b64decode(b64_code).decode()
print(port_str)  # '你好啊'

