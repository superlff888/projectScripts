# -*- coding=utf-8 -*-
# @Time    : 2023/04/06 23:59
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests


def testSoap():
    url = ""
    xml = """<>"""
    headers = {"Content-Type": "text/xml;charset=utf-8"}
    requests.post(url, data=xml, headers=headers)