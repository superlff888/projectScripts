# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 09:31
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests
import yaml

"""
在请求之前，对请求的url进行替换
1、需要二次封装requests，对请求进行定制化
2、将请求的url从一个写死的ip改为一个（任意）的域名
3、使用一个env配置文件，存放各个环境的配置文件
4、然后将请求体中的url替换为`env`配置文件中个人选择的url
5、使用yaml进行管理env配置文件
"""


class Api:

    # 注意：类属性可以用self实例本身去调用，示例： self.env_yml
    env_yml = yaml.safe_load(open("env.yml"))  # 读取yaml流文件数据

    def send(self, data: dict):
        """必须传递一个字典类型参数

        :: param data: Dictionary

        usage::
         >> data = {
                    "method": "get",
                    "url": "http://httpsbin.testing-studio.com/get"
                    }
        >>  确定需要被替换的部分字符串，维护在yml文件中的old字段下，将新环境维护在new字段下
        """
        # 字符串替换，string_obj.replace(__old,__new)
        data["url"] = str(data["url"]).replace(self.env_yml["testing-studio"][self.env_yml["default"]],
                                               self.env_yml["testing-studio"][self.env_yml["override"]])  # 先由dict强转json字符串，然后字符串替换,最后重新赋值于字典key
        r = requests.request(method=data["method"], url=data["url"])
        return r  # r.json()   json格式响应值
