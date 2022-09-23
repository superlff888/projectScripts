# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 11:20
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""单例模式"""

_instance = {}


def single(func):

    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)  # 将实例保存在字典中
            print(f'\n回门实例：{_instance[func]}')
            print(f'\n_instance类型为：{type(_instance)}')
        return _instance[func]
    return wrapper


# def singleton(cls, *args, **kwargs):
#     instances = {}
#
#     def _singleton():
#         if cls not in instances:
#             instances[cls] = cls(*args, **kwargs)
#         return instances[cls]
#
#     return _singleton
#
#
# @singleton
# class MyClass3(object):
#     a = 1
#
#
# one = MyClass3()
# two = MyClass3()
#
# print(id(one))  # 2880466769232
# print(id(two))  # 2880466769232
# print(one == two)  # True
# print(one is two)  # True
