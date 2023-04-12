# -*- coding=utf-8 -*-
# @Time    : 2023/02/03 18:45
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""单例模式"""

def singleton(cls):  # Decorator 装饰器
    # 创建一个字典用来保存类的实例对象;python类变量可以共享类、实例
    _instance = {}
    def _singleton(*args, **kwargs):
        # 先判断这个类有没有对象
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)  # 创建一个对象,并保存到字典当中
        # 将实例对象返回
        return _instance[cls]

    return _singleton


""""""
class Singleton(object):
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = object.__new__(cls)
        return cls._instance

