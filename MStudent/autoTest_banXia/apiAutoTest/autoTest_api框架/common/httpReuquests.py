# @Time  : 2021/06/15 13:56
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================
import os
from urllib.parse import urljoin

import requests

from autoTest_banXia.apiAutoTest.autoTest_api框架.common.logger import Logging
from autoTest_banXia.apiAutoTest.autoTest_api框架.common.read_config import conf_parser_obj


class HttpRequest(object):
    """
    :类作用： 直接发请求，不记录cookies信息
    :params : 适用于get方法
    :data: 表单形式，一般用于post方法
    :json: json格式，用于post方法

    url路径拼接 -->
        Ⅰ举例 url = urljoin(base_url, '/web/userLoginDetail/login')
        Ⅱ举例 url = os.path.join(base_url, '/web/userLoginDetail/login')

    """

    @staticmethod
    def request(method, url, **kwargs):
        """
        ::kwargs return a dict.
        """
        # 统一将请求方法转化为小写字母
        method = method.lower()
        # 判断请求方法
        if method == 'post':
            if not kwargs.get("params"):
                kwargs["params"] = None
            if kwargs.get("data") is None:
                kwargs["data"] = None
            if kwargs.get("json") is None:
                kwargs["json"] = None
            if kwargs.get("cookies") is None:
                kwargs["cookies"] = None
            if kwargs.get("headers") is None:
                kwargs["headers"] = None
            if kwargs.get("files") is None:
                kwargs["files"] = None
            # if kwargs["params"]:
            #     logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["params"]}')
            # if kwargs["data"]:
            #     logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["data"]}')
            # if kwargs["json"]:
            #     logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["json"]}')
            return requests.post(url, **kwargs)
        if method == 'get':
            if not kwargs.get("params"):
                kwargs["params"] = None
            if kwargs.get("data") is None:
                kwargs["data"] = None
            if kwargs.get("json") is None:
                kwargs["json"] = None
            if kwargs.get("cookies") is None:
                kwargs["cookies"] = None
            if kwargs.get("headers") is None:
                kwargs["headers"] = None
            if kwargs.get("files") is None:
                kwargs["files"] = None
            # if kwargs["params"]:
            #     HttpRequest.logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["params"]}')
            # if kwargs["data"]:
            #     HttpRequest.logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["data"]}')
            # return requests.get(url, **kwargs)

class HttpRequestCookies:
    """
    :类作用 :记录cookies信息，提供于下一个请求
    """
    # PATH_LOG = conf_parser_obj.configParser(["logging", "filepath"])
    # LEVEL = conf_parser_obj.configParser(["logging", "level"])
    # # ../表示上一层目录，如当前文件所在目录为common，上层目录为autoTest_api框架，上上层目录为apiAutoTest
    session = requests.sessions.Session()
    # LEVEL = conf_parser_obj.configParser(["logging", "level"])
    # PATH = conf_parser_obj.configParser(["logging", "filepath"])  # ini配置文件中options中key不能维护成path
    # logger = Logging(LEVEL, PATH)  # './logs/shopLog.log'

    def __init__(self):
        # 创建一个session对象，先用session发起登陆请求 ，然后复用该session
        self.method = None
        self.url = None
        self.params = None
        self.data = None
        self.json = None
        self.cookies = None
        self.headers = None
        self.files = None

    def request(self, **kwargs):
        """
        ::kwargs return a dict.

        cookie可能方headers中，也可能放在request body中
        """
        # 统一将请求方法转化为小写字母
        # kwargs["method"].lower()  # self.session.request(**kwargs) 已经封装了

        if kwargs["method"] is None:
            kwargs["method"] = self.method
        if not kwargs["url"]:
            kwargs["url"] = self.data
        if not kwargs.get("params"):
            kwargs["params"] = self.params
        if not kwargs.get("data"):
            kwargs["data"] = self.data
        if not kwargs.get("json"):
            kwargs["json"] = self.json
        if not kwargs.get("cookies"):
            kwargs["cookies"] = self.cookies
        if not kwargs.get("headers"):
            kwargs["headers"] = self.headers
        if not kwargs.get("files"):
            kwargs["files"] = self.files
        # if kwargs["params"]:
        #     # 谁调用该类谁做主，比如BuyerLoginApi继承并调用该类的方法，那么就取最终调用者所在文件的相对位置
        #     # print(f"当前执行文件所在目录的上上层目录下的logs：{os.path.abspath(os.path.dirname(__file__) + '../../logs/shopLog.log')}")
        #     # print(f"当前执行文件所在目录的上层目录的上层目录：{os.path.abspath('../../')}")
        #     self.logger.info(f'正在发送请求...\n请求方法: {self.method},请求参数: {kwargs["params"]}')
        # if kwargs["data"]:
        #     self.logger.info(f'正在发送请求...\n请求方法: {self.method},请求参数: {kwargs["data"]}')
        # if kwargs["json"]:
        #     self.logger.info(f'正在发送请求...\n请求方法: {self.method},请求参数: {kwargs["json"]}')

        return self.session.request(**kwargs)

    # 用完需要关掉（浏览器/session）
    def close(self):
        self.session.close()



