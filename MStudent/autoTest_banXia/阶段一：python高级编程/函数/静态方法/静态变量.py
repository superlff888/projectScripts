# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""


class Message:
    country = "中国"  # 类的变量

    def __init__(self, n):
        self.x1 = n

    @property  # 方法转变属性
    def send(self):
        return "静态方法"

    @staticmethod  # 静态方法并不是真正意义上的类方法，它只是一个被放到类里的函数而已
    def show():
        pass

    @classmethod  # 类方法 一些框架里面有用
    def get_info(cls):
        pass


msg1 = Message("test1")
msg2 = Message("test2")
print(msg1.__dict__)
print(msg2.__dict__)

print(msg2.send)
print(msg2.x1)

print(Message.country)
print(msg1.country)

print(Message.show())
print(msg1.show())

print(Message.get_info())
print(msg2.get_info())