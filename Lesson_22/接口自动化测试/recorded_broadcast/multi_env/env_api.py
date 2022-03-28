# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 09:31
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests

from Lesson_22.接口自动化测试.recorded_broadcast.multi_env import pyEnv_, configMerge
from Lesson_22.接口自动化测试.recorded_broadcast.multi_env.configMerge import envFind


class Api:

    # def __init__(self):
    #     self.env = pyEnv_.env
    #     self.env_conf = configMerge.envFind()
    env = envFind()

    def send(self, data: dict):
        # 字符串替换，只需修改“default”;       self.env["testing-studio"][self.env["default"]]相当于self.env["testing-studio"]["dev"]
        data["url"] = str(data["url"]).replace("httpsbin", self.env["testing-studio"][self.env["default"]])  # 先由dict强转json字符串，然后字符串替换,最后重新赋值于字典key
        r = requests.request(method=data["method"], url=data["url"])
        return r  # r.json()   json格式响应值

