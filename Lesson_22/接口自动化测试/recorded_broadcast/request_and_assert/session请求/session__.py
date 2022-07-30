# -*- coding=utf-8 -*-
# @Time    : 2022/07/31 00:04
# @Author  : ╰☆H.俠ゞ
# =============================================================

from requests import Session

"""

"""


def session_demo():
    data = {
        "phone": "13588888888",
        "password": "123456"
    }
    session = Session()  # 实例化一个session，提供 cookie 持久性、连接池和配置
    session.post(url="http://***.com/login", json=data)  # 先获得cookie
    session.get(url="http://***.com/detail")  # 复用登录的cookie，发送get请求