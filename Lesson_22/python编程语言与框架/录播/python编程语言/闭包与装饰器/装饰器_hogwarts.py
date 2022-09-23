# -*- coding=utf-8 -*-
# @Time    : 2022/09/22 22:59
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""实战场景：利用装饰器实现黑名单"""


def tmp1(func):
    print(func.__name__)
    # # wrapper是用于加强的函数
    def wrapper(arg, kw, **kwargs):  # arg, kw用来接收被装饰函数的所有参数
        print(arg)
        print(kw)
        print(kwargs)
        print("before")
        print(func)
        print(func.__name__)
        func(arg, kw, **kwargs)  # *args, **kwargs
        print("after")
    return wrapper


def tmp2(func):
    print(func.__name__)
    def wrapper(*args, **kwargs):  # wrapper是用于加强的函数
        print(args)  # 被装饰函数的参数组成的元组序列
        print(args[0])  # 被装饰的函数的参数
        print(kwargs)
        print("before")
        print(func)
        print(func.__name__)
        x, y = args  # 解包
        func(x, y, **kwargs)  # *args, **kwargs
        print("after")
    return wrapper


def tmp3(func):
    print(func.__name__)
    def wrapper(*args, **kwargs):  # args以元组序列方式接收被装饰函数的所有参数
        print(args)  # 被装饰函数的参数组成的元组序列
        print(args[0])  # 被装饰的函数的第一个参数
        print(kwargs)
        print("before")
        print(func)
        print(func.__name__)
        func(*args, **kwargs)  # *args, **kwargs
        print("after")
    return wrapper


@tmp1
def a_decorator(x, y, z=None):
    print("a")
    print(f"{x, y, z}")  # 打印一个元组


@tmp2
def b_decorator(x, y, z=None):
    print("a")
    print(f"{(x, y, z)}")


@tmp3
def c_decorator(x, y, z=None):
    print("a")
    print(f"{(x, y, z)}")


a_decorator(10, 20, z=30)
print("=======================================================================\n")
b_decorator(10, 20, z=30)
print("=======================================================================\n")
c_decorator(10, 20, z=30)


