# -*- coding=utf-8 -*-
# @Time    : 2022/07/27 21:01
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests
import urllib3

from Lesson_22.接口自动化测试.interface_test.api_object.apis.utils.loggerMy import logger

"""对底层框架的封装"""


class BaseApi:
    """对发送请求的接口测试工具进行封装"""
    def send_api(self, req, tools="requests"):  # 注意：此处不能用“**req”，调用request时才需要解包
        """
        :: param  tools 如果以后出现比requests更好用的库,可以替换掉requests
        :: param req  url、method、param、data、json
        """
        # logger.info(f"获取到的工具为{tools}")
        if tools == "requests":
            return requests.request(**req)
        if tools == "urllib3":
            pass