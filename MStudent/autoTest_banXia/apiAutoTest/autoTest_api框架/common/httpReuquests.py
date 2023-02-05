# @Time  : 2021/06/15 13:56
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================
import os
from urllib.parse import urljoin

import requests

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.logger import logger


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
    # 创建一个session对象，先用session发起登陆请求 ，然后复用该session
    # 所有接口公用同一个session对象
    session = requests.sessions.Session()

    def __init__(self):
        self.session = HttpRequestCookies.session
        self.logger = logger
        self.method = None
        self.url = None
        self.params = None
        self.data = None
        self.json = None
        self.cookies = None
        self.headers = None
        self.files = None
        self.res = None
        self.desc = None

    def request(self, **kwargs):
        """
        ::kwargs return a dict.
                **kwargs不定长关键字参数，如果调用方传递了kwargs的可变参数，就使用调用方的参数

        cookie可能方headers中，也可能放在request body中

        """
        # 统一将请求方法转化为小写字母
        # kwargs["method"].lower()  # self.session.request(**kwargs) 已经封装了

        if not kwargs.get("method"):  # kwargs为{},kwargs.get("method")返回None; 此处若用kwargs["method"]会报错KeyError
            kwargs["method"] = self.method  # 调用方会重新赋值method(self实例本身，谁调用就是谁)
        if not kwargs.get("url"):
            kwargs["url"] = self.url
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

        # 收集日志  遍历字典收集左右key和value
        for k, v in kwargs.items():
            if kwargs[k]:  # 仅打印不为空的参数
                self.logger.info(f"{self.desc}接口请求中{k}是: {v} ")

        # 获取响应数据   -->  响应状态码和响应文本
        try:
            self.res = self.session.request(**kwargs)  # **kwargs中关键字个数跟调用方有关
            self.logger.info(f"{self.desc}接口的响应状态码: {self.res.status_code}")
            # self.logger.info(f"接口的响应文本: {self.res.text}")
        except Exception as e:
            self.logger.exception("接口发送错误!")
            raise e
        return self.res

    # 用完需要关掉（浏览器/session）
    def close(self):
        self.session.close()



