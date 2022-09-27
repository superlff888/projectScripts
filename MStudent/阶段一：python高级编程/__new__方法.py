# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 14:03
# @Author  : ╰☆H.俠ゞ
# =============================================================
class Person(object):

    def __new__(cls):
        print(f"super是：{super()}")
        print(f"super type是：{type(super())}")
        print(f"object是：{type(object())}")
        print("__new__ called")
        instance = super().__new__(cls)
        print(f"instance: {type(instance)}")
        print(instance)
        print(id(instance))
        return instance  # 若不返回一个实例对象的话，则不会调用init方法

    def __init__(self):
        print("__init__ called")
        print(id(self))


b = Person()

"""
实例6：在重写__new__()方法时，需要在参数中加入*args,**kwargs，或者显式地加入对应的参数，才能通过__init__()方法初始化参数。
"""


class Person(object):

    def __new__(cls, *args, **kwargs):  # Or def __new__(cls, name)
        print("__new__ called")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        print("__init__ called")
        self.name = name


e = Person("Eric")
print(e.name)
