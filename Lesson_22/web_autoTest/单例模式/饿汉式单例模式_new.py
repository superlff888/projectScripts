# -*- coding=utf-8 -*-
# @Time    : 2023/01/31 18:50
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""
饿汉式单例模式：类加载过程中创建实例
"""


class IDMaker:
    # python类变量可以被多个类、实例对象共享
    __instance = None
    _ID = -1

    # 类加载阶段，通过父类的new方法创建当前类的实例（需要调用__init__方法才能重新构建实例，即给new出的实例添加属性，当然也可不重新构建）
    # python 在加载阶段，通过父类的__new__创建实例；如果重写__new__,就不会调用父类的__new__方法
    def __new__(cls):
        if cls.__instance is None:  # 相当于cls.__instance is None
            # 调用父类__new__,将当前类的类名作为父类new方法的参数，用以创建当前类的实例对象，此时该实例对象没有任何属性，若需属性需要__init__
            cls.__instance = super().__new__(cls)
        else:
            cls._ID += 1
        return cls.__instance  # __new__方法需要返回一个实例，否则就不会调用__init__进行实例化,因为__init__(self)需要接收new出的实例对象

    def get_id(self):
        self._ID += 1
        return self._ID


def test_IDMaker():
    # IDMaker 单例类，只允许有一个实例
    id1 = IDMaker().get_id()
    id2 = IDMaker().get_id()  # 第二次及以后new实例时，就不会调用父类new创建新的实例了；内存中已经有了第一次初始化new的实例
    id3 = IDMaker().get_id()
    print(id1, id2, id3)



