# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 11:20
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""单例模式"""


def single(func):
    _instance = {}
    print(f'初始实例为：{_instance}')
    def wrapper(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func(*args, **kwargs)
            print(f'回门实例：{_instance[func]}')
        return _instance[func]
    return wrapper


@single
class A:
    def __init__(self):
        print("pass")


# print(f"未导入：{id(A())}")
# print(f"未导入：{id(A())}")
if __name__ == "__main__":
    A()