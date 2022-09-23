# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 11:20
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""单例模式: 将实例保存在字典中，若类(内存地址)不在字典中，则会重新实例化放进字典中"""
_instance = {}


def single(func):
    # _instance = {}
    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)  # 将实例保存在字典中
            print(f'\n回门实例：{_instance[func]}')
            print(f'\n_instance类型为：{type(_instance)}')
        return _instance[func]
    return wrapper

