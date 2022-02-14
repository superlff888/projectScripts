# @Time  : 2022/01/26 09:52
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
from types import MethodType


# class A:
#     def a1(self):
#         return id(self)
#
#     def a2(self):
#         print("")
#
#
# print(id(A().a1()))
# print(id(A().a1()))
# print(id(A().a1()))
# print(id(A().a2()))
# print(id(A().a2()))


"""
给一个实例绑定的方法，对另一个实例是不起作用的
"""


class Func:

    def __init__(self):
        self.num = None

    def func(self):
        print("绑定方法")

    @classmethod
    def func_cls(cls, name):
        print(f"名字是{name}")


def func1(self, num):
    self.num = num


def func_cls(self, name):
    print(f"我的名字是{name}")


f1 = Func()
f2 = Func()
f1.func1 = MethodType(func1, f1)  # 给实例f绑定一个方法
f1.func1(10)
# f2.func1()  # 'Func' object has no attribute 'func1'
print(f1.num)


# 给class绑定方法后，所有实例均可调用
Func.func_cls = func_cls  # 给class绑定一个方法
f1.func_cls('lee')
f2.func_cls('john')


"""
【使用__slots__】
    1、更快的属性访问速度
    2、减少内存消耗
"""


# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student:
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
    name = None
    age = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def func_demo(self):
        pass


s = Student('lee', 18)

# s.weigh = 65  # 'Student' object has no attribute 'weigh'

"""
注意全局变量、类变量、局部变量的区别
"""