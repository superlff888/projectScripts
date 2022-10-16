# @Time  : 2022/01/29 13:38
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
"""
__str__
此函数必须有返回值，而且return后只能接受字符串数据
参数赋值时，调用该函数，且只调用一次!只调用一次!只调用一次!
"""


class Person:
    def __init__(self, name, age, address):  # name, age, address
        self.name = name
        self.age = age
        self.address = address
        # name = 'lee'
        # age = 'lee'

    def details(self):
        print('名字：' + self.name + ',年龄：' + str(self.age) + ', 籍贯：' + self.address)
        return 'a', 'b', 'c'

    # 重写_str__函数
    def __str__(self):
        print('我是__str__函数...')
        # return后只能接受字符串数据,返回多个str组成的元组
        return '名字：' + self.name + ',年龄：' + str(self.age) + ', 籍贯：' + self.address


# 实例化对象
p = Person('Joy', 25, '北京')  # 'Joy', 25, '北京'
# print(p.__str__())  # 运行结果同print(p)，但前提是必须有return
print(p)  # 实例化对象时，自动调用__str__,d等同于print(p.__str__())
# tuple_p = p.details()
# a, b, c = tuple_p
# print(p.details())
# print(a)
# print(b)
# print(c)
