# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 09:31
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests
import yaml
from Lesson_22.接口自动化测试.recorded_broadcast.multi_env import pyEnv_, configMerge


class Api:
    # 注意：类属性可以用self去调用，示例： self.env_yml, 可不用构方法初始化
    env_yml = yaml.safe_load(open("./env.yml"))  # 读取yaml流文件数据
    env_py = pyEnv_.env  # 直接从py文件中取值
    env_conf = configMerge.envFind()  # 封装了读取yaml流文件数据的方法

    # def __init__(self):
    #     self.env_py = pyEnv_.env  # 直接从py文件中取值
    #     self.env_conf = configMerge.envFind()  # 封装了读取yaml流文件数据的方法

    def send(self, data: dict):
        # 字符串替换，只需修改“default”;       self.env["testing-studio"][self.env["default"]]相当于self.env["testing-studio"]["dev"]
        data["url"] = str(data["url"]).replace("httpsbin", self.env_yml["testing-studio"][self.env_yml["default"]])  # 先由dict强转json字符串，然后字符串替换,最后重新赋值于字典key
        r = requests.request(method=data["method"], url=data["url"])
        return r  # r.json()   json格式响应值

