# -*- coding=utf-8 -*-
# @Time    : 2022/07/27 20:49
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""
不管哪一个接口都需要获取token
"""
import requests

from Lesson_22.接口自动化测试.interface_test.api_object.apis.base_api.base_api import BaseApi


class Wework(BaseApi):
    def __init__(self):
        self.token = None  # 可以不事先定义self.token，只是这样更规范
        self.get_token()  # 实例化时，自动调用get_token
        print("已获取token")

    def get_token(self):
        # return： access_token的值
        corpid = 'wwba697e4878807a9f'
        corpsecret = '631qSHbvs5vyhpFQmp7a5BZDkxkfBEF3Ev3VEV-DJNw'
        # 注意：解包对象为字典；url、param要加引号表示字符串
        req = {
                "method": "GET",
                "url": 'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
                "params": {
                    "corpid": corpid,
                    "corpsecret": corpsecret
                    }
                }
        # 发起get请求，获取token
        res = self.send_api(req)  # 实例化时自动调用send_api()方法
        print(f"获取token：{res.json()}")
        self.token = res.json()["access_token"]  # res有返回值,相当于对self.token重新赋值

