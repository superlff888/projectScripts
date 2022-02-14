# @Time  : 2022/01/24 21:09
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

# 类型提示功能
from typing import List


def greeting(name: str) -> str:  # name: str 指明入参类型; -> str 指定返回数据类型
    return 'Hello ' + name.split(',')[1]  # 字符串拼接;指定数据类型后，对应数据类型的方法就会联想出来，方便调用


a = greeting("java, python")
print(f'greeting返回值为： {a}')

'''
1、增强代码的可读性
2、联想功能
'''

# 为类型起别名

vector = List[float]  # 定义一个元素为float数据类型的列表


def scale(scalar: float, v: vector) -> vector:
    print(f'scale入参为：{scalar, v}')
    return [scalar * num for num in v]


vector = scale(2.0, [1.2, 1.1, 3])
print(f'scale函数返回结果为：{vector}')


# 设置提示类型

class Student:
    name: str
    age: int

    def eat(self):
        print("吃东西")


def get_st(name: str, age: int) -> Student():  # 返回自定义的提示类型
    return Student()


get_st('lee', 18).eat()  # 联想出返回的类的属性和方法
