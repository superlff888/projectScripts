# -*- coding=utf-8 -*-
# @Time    : 2022/07/31 10:15
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.请求构造.验证链式调用return的函数.MyRequest import Request


def POST(url, payload=None, json=None):
    return Request(url, data=payload, json=json)


POST("江苏", 18, ["丰满", "美丽"])

