# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 23:17
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json

import jsonpath
import requests

from common._logger import logger

class HttpClient:
    # 类属性 所有接口共用一个session
    session = requests.sessions.Session()

    def __init__(self):
        """None代表没传参"""
        self.logger = logger
        self.session = HttpClient.session
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None

    def send(self, **kwargs):

        if not kwargs.get("url"):  # 必须用get，不然会报错
            kwargs["url"] = self.url

        if not kwargs.get("method"):
            kwargs["method"] = self.method

        if not kwargs.get("headers"):
            kwargs["headers"] = self.headers

        if kwargs.get('params') is None:
            kwargs['params'] = self.params

        if kwargs.get('data') is None:
            kwargs['data'] = self.data

        if kwargs.get('json') is None:
            kwargs['json'] = self.json

        if kwargs.get('files') is None:
            kwargs['files'] = self.files
        # 请求
        for k, v in kwargs.items:
            if kwargs[k]:  # not None
                self.logger.info(f'接口{k}是:{v}')
        # 响应
        try:
            self.res = self.session.request(**kwargs)
            self.logger.info(f'接口的响应状态码：{self.resp.status_code}')
            self.logger.info(f'接口的响应信息是：{self.resp.text}')
        except Exception as e:
            self.logger.info("接口请求错误")
            raise e
        return self.res

    def parse_json(self, express, index: int = 0):
        """
        :param  express  jsonpath表达式
        :param  index  返回`result`列表下标，默认取第一个
        """
        text = self.res.text  # 获取接口响应文本，有可能返回的是空字符串
        if text != '':
            try:
                res_dict = json.loads(text)  # 转换成python对象dict
                if index < 0:  # 提取全部
                    result = jsonpath.jsonpath(res_dict, express)
                    self.logger.info(f'通过{express}从{text}中提取结果{result}')
                    return result
                else:
                    result = jsonpath.jsonpath(res_dict, express)[index]
                    self.logger.info(f'通过{express}从{text}中提取结果{result}')
                    return result
            except Exception as e:
                self.logger.exception(f"通过jsonpath'{express}'从{text}提取时抛出异常……")
                raise e

