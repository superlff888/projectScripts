# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 17:21
# @Author  : ╰☆H.俠ゞ
# =============================================================
class Person(object):
    def __init__(self):
        self.age = 10

    @property  # 会自动产生两个装饰器age.setter（xx.setter）和 age.del（xx.del）
    def age(self):
        return self._age

    @age.setter  # 进行设置 age 的时候自动调用
    def age(self, _age):
        if 0 < _age < 100:
            self._age = _age
        else:
            raise ValueError("年龄不在范围内")

    @age.deleter
    def age(self):
        print("ok ok")


p = Person()
p.age = 20
print(p.age)
p.age = 1
print(p.age)
del p.age