# -*- coding=utf-8 -*-
# @Time    : 2023/02/03 10:00
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.httpReuquests import HttpRequestCookies


class BaseSellerApi(HttpRequestCookies):
    """作为所有功能类的父类"""
    # 定义类属性，实现全局调用
    seller_token = ''
    seller_uid = ''

    def __init__(self):
        # 获取父类属性
        super().__init__()
        # 部分属性重新赋值
        self.host = 'http://www.mtxshop.com:7003'
        self.headers = {"Authorization": BaseSellerApi.seller_token, "Content-Type": "application/json"}
        self.uid = BaseSellerApi.seller_uid
