# -*- coding=utf-8 -*-
# @Time    : 2023/01/31 17:39
# @Author  : ╰☆H.俠ゞ
# =============================================================

from singleton import s as s1, singleton_dec
from singleton import s as s2


# Method One：通过导入模块实现
def show_method_one():
    """

    :return:
    """
    print("方法1:")
    print(s1)
    print(s2)
    print(id(s1))
    print(id(s2))
    print("=============================================\n")


show_method_one()


@singleton_dec
class Demo2(object):
    a = 1

    def __init__(self, x=0):
        self.x = x


a1 = Demo2(1)
a2 = Demo2(2)
print("方法2:")
print(id(a1))
print(id(a2))
print("=============================================\n")


