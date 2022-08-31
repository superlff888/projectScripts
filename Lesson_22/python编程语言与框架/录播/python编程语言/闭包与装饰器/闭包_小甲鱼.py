# -*- coding=utf-8 -*-
# @Time    : 2022/08/30 16:58
# @Author  : ╰☆H.俠ゞ
# =============================================================
# 外函数中会return内函数的内存地址,内部函数内存地址当作值传递给外部变量，这样内部函数可以访问外围的变量
import random


def power(exp):
    def exp_of(base):
        return base ** exp

    return exp_of


square = power(2)
print(square(3))


"""
内部函数也可以改写外部函数(外层函数作用域)的变量值，但需要使用nonlocal关键词声明这是外部的变量
"""


def outer():
    x = 0
    y = 0
    def inner(x1, y1):
        nonlocal x, y
        x += x1
        y += y1
        print(f"现在，x={x},y={y}")
    return inner


moved = outer()
moved(1, 2)  # x=1,y=2
moved(-1, 1)  # x=0,y=3

print("============================================\n")
"""
应用场景: 把每次移动到的那个坐标位置保存下来
"""

origin = (0, 0)  # 这是原点
legal_x = [-100, 100]  # 限定x轴的移动范围
legal_y = [-100, 100]  # 限定y轴的移动范围


def create(pos_x=0, pos_y=0):
    def moving(direction: list, step: int):
        nonlocal pos_x, pos_y  # 关键词声明这是外部的变量
        new_x = pos_x + direction[0] * step  # 方向乘以步进值
        new_y = pos_x + direction[1] * step  # 方向乘以步进值

        if new_x < legal_x[0]:
            pos_x = legal_x - (new_x - legal_x[0])
        elif new_x > legal_x[1]:
            pos_x = legal_x[1] - (new_x - legal_x[1])
        else:
            pos_x = new_x

        if new_y < legal_y[0]:
            pos_y = legal_y - (new_y - legal_y[0])
        elif new_y > legal_y[1]:
            pos_y = legal_y[1] - (new_y - legal_y[1])
        else:
            pos_y = new_y
        return pos_x, pos_y
    return moving  # 返回内层函数的内存地址，供引用


move = create()
print(move([1, 0], 20))
print(move([1, 1], 10))
