# -*- coding=utf-8 -*-
# @Time    : 2023/01/31 17:38
# @Author  : ╰☆H.俠ゞ
# =============================================================


class Singleton(object):
    def __init__(self, name):
        self.name = name

    def run(self):
        print(self.name)


s = Singleton("Tom")


"""
ck15  测试框架4  单例 模式
"""


# Method Two：通过装饰器实现;
# 被装饰的类为单例类，单例类只有一个实例
def singleton_dec(cls):  # Decorator 装饰器
    # 创建一个字典用来保存类的实例对象;python类变量可以共享类、实例
    _instance = {}

    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton