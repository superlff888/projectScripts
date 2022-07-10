# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 22:03
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint
import requests


"""
需要打开charles
特别注意：关闭全局代理，即proxy >> Windows Proxy
"""


class Test_timeout:
    """设置超时时间，是为了防止接口一直执行，阻碍其他接口执行"""

    def setup_class(self):
        self.proxy = {"http": "http://127.0.0.1:8811", "https": "https://127.0.0.1:8811"}

    def test_timeout_00(self):
        res = requests.get('http://httpbin.testing-studio.com/get')
        print(f'\n{res.json()}')

    def test_timeout_01(self):
        res = requests.get('http://httpbin.ceshiren.com/get')
        print(f'\n{res.json()}')

    def test_timeout_02(self):
        # 在charles打断点，模拟请求超时；若不设置请求超时时间，则会一直等待接口响应，阻碍程序代码顺序向下执行
        res = requests.post('http://httpbin.ceshiren.com/post', timeout=2, proxies=self.proxy,
                            verify=False)  # 取消verify认证（类似于信任证书）
        print(f'\n{res.json()}')

    def test_timeout_03(self):
        res = requests.get('http://httpbin.ceshiren.com/get')
        print(f'\n{res.json()}')
