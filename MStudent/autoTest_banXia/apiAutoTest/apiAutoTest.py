# -*- coding=utf-8 -*-
# @Time    : 2023/01/28 15:20
# @Author  : ╰☆H.俠ゞ
# =============================================================


import requests

session = requests.session()


def login():
    url = r'http://82.156.74.26:9088/pinter/pinter/bank/api/login'
    payload = {'userName': 'admin', 'password': '1234'}
    res = session.post(url=url, data=payload)
    print(res.json())


