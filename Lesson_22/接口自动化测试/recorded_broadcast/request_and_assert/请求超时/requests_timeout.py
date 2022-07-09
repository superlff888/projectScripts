# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 22:03
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint
import requests


"""
需要打开charles
"""


class Test_timeout:
    """设置超时时间，是为了防止接口一直执行，阻碍其他接口执行"""

    def setup_class(self):
        self.proxy = {"http": "http://127.0.0.1:8811", "https": "https://127.0.0.1:8811"}

    def test_timeout_01(self):
        # urllib3.disable_warnings()
        res = requests.get('http://httpbin.testing-studio.com/get', proxies=self.proxy,
                           verify=False)  # 取消verify认证（类似于信任证书）
        print(f'\n{res.json()}')

    def test_timeout_02(self):
        # urllib3.disable_warnings()
        res = requests.post('http://httpbin.testing-studio.com/post', timeout=2, proxies=self.proxy,
                            verify=False)  # 取消verify认证（类似于信任证书）
        print(f'\n{res.json()}')

    def test_timeout_03(self):
        res = requests.get('http://ceshiren.com/categories.json', proxies=self.proxy,
                           verify=False)  # 取消verify认证（类似于信任证书）
        print(f'\n{res.json()}')
