
# @Time  : 2021/06/15 13:56
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================
import json
import jsonpath
import requests
from common.my_logger import logger


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

        # 请求入参日志收集
        for k, v in kwargs.items():  # 遍历字典收集请求参数所有key和value
            if kwargs[k]:  # 仅打印不为空的参数
                self.logger.info(f"{self.desc}接口请求入参中的{k}是: {v} ")

        # 响应数据日志收集 --> 响应状态码和响应文本
        try:
            self.res = self.session.request(**kwargs)  # **kwargs中关键字个数跟调用方有关
            self.logger.info(f"\t{self.desc}接口的响应状态码: {self.res.status_code}")
            self.logger.info(f"\t{self.desc}接口的响应文本: {self.res.text}")
        except Exception as e:
            self.logger.exception("接口发送错误!")
            raise e
        return self.res

    # 定义接口响应数据jsonpath提取方法
    def extract_json(self, express, index: int = 0):
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

    # 用完需要关掉（浏览器/session）
    def close(self):
        self.session.close()


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
    def __init__(self):
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
        将调用者init初始化的属性值赋值于kwargs

        ::kwargs kwargs is a dict.
        """

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
            # 收集日志  遍历字典收集所有key和value
        for k, v in kwargs.items():
            if kwargs[k]:  # 仅打印不为空的参数
                self.logger.info(f"{self.desc}接口请求中{k}是: {v} ")

    # 获取响应数据   -->  响应状态码和响应文本
        try:
            self.res = requests.request(**kwargs)  # **kwargs中 关键字的个数 跟调用方有关
            self.logger.info(f"\t{self.desc}接口的响应状态码: {self.res.status_code}")
            self.logger.info(f"接口的响应文本: {self.res.text}")
        except Exception as e:
            self.logger.exception("接口发送错误!")
            raise e
        return self.res

