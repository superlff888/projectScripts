# -*- coding=utf-8 -*-
# @Time    : 2023/01/31 19:26
# @Author  : ╰☆H.俠ゞ
# =============================================================
from threading import Lock


"""
懒汉式单例：类使用中创建实例
"""


class IDMaker:
    # 申请一个线程锁（还未被调用）
    __instance_lock = Lock()
    # python类变量可以被多个类、实例对象共享
    __instance = None
    _ID = 0

    # 类加载阶段，通过父类的new方法创建当前类的实例（需要调用__init__方法才能初始化构建实例，即给new出的实例添加属性，当然也可不重新构建）
    # python 在加载阶段，通过父类的__new__创建实例；如果重写__new__,就不会调用父类的__new__方法
    def __new__(cls):
        raise ImportError("Instantition not allow")

    @classmethod
    def get_instance(cls):
        # with会帮我们自动上锁和释放
        with cls.__instance_lock:  # 添加线程锁，同一时间只允许一个线程运行
            if not cls.__instance:
                cls.__instance = super().__new__(cls)
        return cls.__instance

    def get_id(self):
        self._ID += 1
        return self._ID


def test_IDMaker():
    # IDMaker 单例类，只允许有一个实例
    id1 = IDMaker.get_instance().get_id()
    id2 = IDMaker.get_instance().get_id()
    id3 = IDMaker.get_instance().get_id()
    print(id1, id2, id3)
