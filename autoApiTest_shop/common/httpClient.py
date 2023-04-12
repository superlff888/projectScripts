# !/usr/bin python3                                 
# encoding: utf-8 -*-
import json

import jsonpath
import requests

from common.logger import logger


class RequestsClient:
    # 类属性  作用全局变量使用  所有的接口共用同一个session对象
    session = requests.session()

    def __init__(self):
        # 收集日志
        self.logger = logger
        # 类直接调用类属性
        self.session = RequestsClient.session
        self.url = None
        self.method = None
        self.headers = None
        self.params = None
        self.data = None
        self.json = None
        self.files = None
        self.resp = None

    # 不确定 接口传递哪个参数,不确定传几个，通过不定长参数传递
    # **kwargs 不定长关键字参数，可以在接口默认值针对一些参数定义
    # 如果调用方传递了kwargs的可变参数，就使用调用方法的
    # **kwargs 返回是字典
    def send(self, **kwargs):
        if kwargs.get('url') is None:
            kwargs['url'] = self.url

        if kwargs.get('method') is None:
            kwargs['method'] = self.method

        if kwargs.get('headers') is None:
            kwargs['headers'] = self.headers

        if kwargs.get('params') is None:
            kwargs['params'] = self.params

        if kwargs.get('data') is None:
            kwargs['data'] = self.data

        if kwargs.get('json') is None:
            kwargs['json'] = self.json

        if kwargs.get('files') is None:
            kwargs['files'] = self.files

        # 收集日志  遍历字典收集所有key和value
        for key, value in kwargs.items():
            self.logger.info(f'接口{key}是:{value}')
        # 获取关键响应数据 -- 响应状态码和响应文本
        # 异常处理
        try:
            self.resp = self.session.request(**kwargs)
            self.logger.info(f'接口的响应状态码：{self.resp.status_code}')
            self.logger.info(f'接口的响应信息是：{self.resp.text}')
        except Exception as e:
            self.logger.exception('接口发送错误')
            raise e
        return self.resp

    # 定义接口响应数据jsonpath提取方法
    def extract_json(self, express, index: int = 0):
        """
        :param  express  jsonpath表达式
        :param  index  返回`result`列表的下标，默认取第一个
        """
        text = self.resp.text  # 获取接口响应文本，有可能返回的是空字符串
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
