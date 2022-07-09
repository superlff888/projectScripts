# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 22:55
# @Author  : ╰☆H.俠ゞ
# =============================================================

import requests
import urllib3


urllib3.disable_warnings()  # 仅移除警告

proxy = {"http": "http://127.0.0.1:8811", "https": "https://127.0.0.1:8811"}

requests.post(url='https://httpbin.testing-studio.com/post', proxies=proxy, verify=False)  # 需要打开charles
