# @Time  : 2022/01/29 13:27
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
"""
 每一次属性赋值时, __setattr__都会被调用;
 由于每次类实例进行属性赋值时都会调用__setattr__()，所以可以重载__setattr__()方法，来动态的观察每次实例属性赋值时__dict__()的变化

"""


# 用__setattr__析构函数
class Fun(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.male = False

    # 重写父类方法
    def __setattr__(self, key, value):
        """
        每次实例属性赋值时，自动调用该方法，并将对应key、value传给该方法，注册到__dict__字典中
        """
        self.__dict__[key] = value  # 属性注册

        print("*" * 50)
        print("setting:{},  with:{}".format(key, value))
        print("current __dict__ : {}".format(self.__dict__))


fun = Fun("Liu", 12)
