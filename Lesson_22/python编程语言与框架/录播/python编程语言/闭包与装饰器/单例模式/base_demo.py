# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 14:43
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.python编程语言与框架.录播.python编程语言.闭包与装饰器.单例模式.singleon import single


@single
class Base:
    def __init__(self):
        print("pass")

    def eat(self):
        print("我要吃饭")

    def sleep(self):
        print("睡觉")

    def jump(self):
        print("跳转")


