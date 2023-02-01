# -*- coding=utf-8 -*-
# @Time    : 2022/07/29 23:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
class Person(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print("实例对象:%s" % self.name, id(self))
        print("python解释器开始回收%s对象了" % self.name)  # 从内存清除掉


# print("类对象", id(Person))
zhangsan = Person("张三")
print("实例对象张三:", id(zhangsan))
print("------------")
lisi = Person("李四")
print("实例对象李四:", id(lisi))
