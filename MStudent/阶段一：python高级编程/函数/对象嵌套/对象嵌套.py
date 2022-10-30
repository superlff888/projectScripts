# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""


class Stu:
    pass


class Classes:
    def __init__(self, name) -> None:
        self.name = name
        self.stus = []

    def add(self, stu: Stu):
        self.stus.append(stu)


if __name__ == '__main__':
    c = Classes("1班")
    print(c.name)

    s1 = Stu()
    s1.name = "张三"
    s1.age = 30
    print(s1.__dict__)  # 将属性以字典形式展示出来
    c.add(s1)  # 将s1对象追加进去了

    s2 = Stu()
    s2.name = "张三"
    s2.age = 30
    s2.sex = "男"
    c.add(s2)
    print(f"stus为：{c.stus}")
    for stu in c.stus:
        # __dict__是类的内置属性，用于以字典的形式存储类里的属性
        print(stu.__dict__)