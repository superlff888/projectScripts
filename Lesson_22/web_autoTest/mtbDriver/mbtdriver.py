# -*- coding=utf-8 -*-
# @Time    : 2022/08/07 14:19
# @Author  : ╰☆H.俠ゞ
# =============================================================
import importlib

"""
动态导入和反射
"""


def a():
    """__name__  入口函数，用来区分当前模块是独立运行还是被调用"""
    print(str(__name__).split(".")[-1] + '.yaml')


m = importlib.import_module("test__name__")
func = getattr(m, "test_a")  # getattr(x, 'y') 等价于 x.y
func()  # 执行函数需加括号 m.test_a()
print(id(func))
print(id(func))