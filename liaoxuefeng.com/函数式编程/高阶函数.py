# @Time  : 2021/05/20 15:38
# @Author    : House Lee
# -*-coding=utf-8-*-

"""
函数也可以做为变量
"""


def add(x, y, f):
    return f(x) + f(y)


print(add(2, -6, abs))
