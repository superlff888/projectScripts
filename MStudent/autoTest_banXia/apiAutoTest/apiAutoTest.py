# -*- coding=utf-8 -*-
# @Time    : 2023/01/28 15:20
# @Author  : ╰☆H.俠ゞ
# =============================================================
import csv

import pymysql
import pytest
import requests

session = requests.session()
IP = 'http://82.156.74.26:9088'


def login():
    url = IP + '/pinter/bank/api/login'
    payload = {'userName': 'admin', 'password': '1234'}
    res = session.post(url=url, data=payload)
    print(res.json())


def query():
    URL = IP + '/pinter/bank/api/query'
    param = {'userName': 'admin'}
    res = session.get(url=URL, params=param)
    print(res.text)


def test_demo():
    pytest.assume(1 == 2, "攀岩失败")


login()
query()


