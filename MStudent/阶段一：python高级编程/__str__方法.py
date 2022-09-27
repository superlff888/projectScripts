# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 14:39
# @Author  : ╰☆H.俠ゞ
# =============================================================


class Cat:
    a = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def __str__(self):
        return "输出对象"


c = Cat("TOM", 5)
print(c)
print(Cat.a)


