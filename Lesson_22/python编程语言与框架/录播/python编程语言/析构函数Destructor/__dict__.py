# @Time  : 2022/01/29 14:44
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
"""
每次实例属性赋值时，都会将属性名和对应值存储到__dict__字典中
"""


class AnotherFun:
    def __init__(self):
        self.name = "Liu"
        print(self.__dict__)
        self.age = 12
        print(self.__dict__)
        self.male = True
        print(self.__dict__)


another_fun = AnotherFun()
