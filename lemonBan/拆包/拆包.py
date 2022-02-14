# @Time  : 2021/06/18 14:53
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
元组_(列表)拆包
"""

# def func():
#     return 1, 2, 3


# print(func())  # (1, 2, 3)
# res = func()
# a, b, c = func()
# print(a)
# print(b)
# print(c)

res = (1, 2, 3)
res1 = [1, 2, 3]


def test(x, y, z):
    return x + y + z


# 利用*对元组拆包：只能再函数调用的时候去使用
print(test(*res))
print(test(*res1))

"""
字典拆包,将value作为实参传进去
"""
dict_a = {'x1': 1,
          'y1': 2,
          'z1': 3}


def test(x1, y1, z1):
    print(x1)
    print(y1)
    print(z1)
    return x1, y1, z1


print(test(**dict_a))


