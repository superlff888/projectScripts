# -*- coding=utf-8 -*-
# @Time    : 2022/08/31 14:37
# @Author  : ╰☆H.俠ゞ
# =============================================================


"""
装饰器：金钟罩铁布衫
"""

import time


def time_master(func):
    def call_func():
        print("程序开始运行……")
        start = time.time()
        func()
        stop = time.time()
        print(f"程序已经运行了{(stop-start):.2f}秒")
    return call_func


@time_master
def myFunc():
    time.sleep(2)
    print("程序正在运行~")
    print("hello,world")


myFunc()


"""多个装饰器"""


def square(func):
    def inner():
        x = func()
        return x * x
    return inner


def cube(func):
    def inner():
        x = func()
        return x * x * x
    return inner


@cube  # 装饰器从里到外执行
@square
def test():
    return 2


print(test())  # 添加装饰器后，return结果发生变化
