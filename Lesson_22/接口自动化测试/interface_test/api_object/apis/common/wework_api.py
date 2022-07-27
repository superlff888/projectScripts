# -*- coding=utf-8 -*-
# @Time    : 2022/07/27 20:49
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""
不管哪一个接口都需要获取token
"""
import requests


class Wework:
    def __init__(self):
        self.token = None
        self.get_token()  # 实例化时，自动调用get_token
        print("已获取token")

    def get_token(self):
        # return： access_token的值
        corpid = 'wwba697e4878807a9f'
        corpsecret = '631qSHbvs5vyhpFQmp7a5BZDkxkfBEF3Ev3VEV-DJNw'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        param = {
            "corpid": corpid,
            "corpsecret": corpsecret
        }

        # 发起get请求，获取token
        res = requests.get(url=url, params=param)
        print(f"获取token：{res.json()}")
        self.token = res.json()["access_token"]  # res有返回值
