# -*- coding=utf-8 -*-
# @Time    : 2022/07/08 23:56
# @Author  : ╰☆H.俠ゞ
# =============================================================


import requests

"""
requests没有封装xml，所以需要额外配置下headers，指定Content-Type为application/xml
"""

xml = """<?xml version='1.0' encoding='utf-8'?><a>6</a>"""
header = {
    'Content-Type': 'application/xml'  # 默认Content-Type:application/json
}

res = requests.post('http://httpbin.org/post', data=xml, headers=header)
print(res.text)

