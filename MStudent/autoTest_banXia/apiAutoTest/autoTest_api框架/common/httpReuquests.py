# @Time  : 2021/06/15 13:56
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================
import os
from urllib.parse import urljoin

import requests


from autoTest_banXia.apiAutoTest.autoTest_api框架.common.logger import logger


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
            if kwargs["params"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["params"]}')
            if kwargs["data"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["data"]}')
            if kwargs["json"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["json"]}')
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
            if kwargs["params"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["params"]}')
            if kwargs["data"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["data"]}')
            return requests.get(url, **kwargs)

class HttpRequestCookies:
    """
    :类作用 :记录cookies信息，提供于下一个请求
    """

    def __init__(self):
        # 创建一个session对象，先用session发起登陆请求 ，然后复用该session
        self.session = requests.sessions.Session()

    def request(self, method, url, **kwargs):
        """
        ::kwargs return a dict.

        cookie可能方headers中，也可能放在request body中
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
            if kwargs["params"]:
                # 谁调用该类谁做主，比如BuyerLoginApi继承并调用该类的方法，那么就取最终调用者所在文件的相对位置
                # print(os.path.abspath("../../logs/shopLog.log"))
                print(f"当前执行文件所在目录的上上层目录下的logs：{os.path.abspath(os.path.dirname(__file__) + '../../logs/shopLog.log')}")
                print(f"当前执行文件所在目录的上层目录的上层目录：{os.path.abspath('../../')}")
                # print(os.path.abspath('\n'))
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["params"]}')
            if kwargs["data"] is not None:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["data"]}')
            if kwargs["json"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["json"]}')
            return self.session.post(url, **kwargs)
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
            if kwargs["params"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["params"]}', _srcfile=True)
            if kwargs["data"]:
                logger.info(f'正在发送请求...\n请求方法: {method},请求参数: {kwargs["data"]}')
            return self.session.get(url, **kwargs)

    # 用完需要关掉（浏览器/session）
    def close(self):
        self.session.close()



