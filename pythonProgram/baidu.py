# -*- coding=utf-8 -*-
# @Time    : 2023/03/22 22:14
# @Author  : ╰☆H.俠ゞ
# =============================================================
from functools import reduce

"""1、编写一个程序，查找所有此类数字，它们可以被7整除，但不能是5的倍数（在2000和3200之间（均包括在内））。获得的数字应以逗号分隔的顺序打印在一行上"""

# # 使用for循环
#
# l = []
# for i in range(2000, 3201):
#     if i % 7 == 0 and i % 5 != 0:
#         # print(i, end=",")
#         l.append(str(i))
#
# l.sort(reverse=True)
# print(l)
# str_a = ",".join(l)
# print(str_a)
#
# # 列表推导式；
# print("列表：", end="")
# print(*sorted([i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0], reverse=False), sep=',')
# print(*(sorted([i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0], reverse=False)), sep=",")
#
# """
# 【生成器】
# generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，
# 在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
# """
# g = (i for i in range(10))
# print(next(g))
# print(next(g))
# print(g.__next__())
#
#
# # 斐波拉契
# def fib(x):
#     n, a, b = 0, 0, 1
#     while n < x:
#         print(a)
#         a, b = b, a + b
#         n += 1
#     return "done"
#
#
# print("==============================")
# fib(5)
#
#
# # 斐波那契形式的生成器：调用一个generator函数将返回一个generator
# def fibs(x):
#     n, a, b = 0, 0, 1
#
#     while n < x:
#         yield b
#         a, b = b, a + b
#         n += 1
#     # return "done"
#
#
# """编写一个程序，可以计算给定数字的阶乘，结果应以逗号分隔的顺序打印在一行上，假设向程序提供了以下输入：8然后，输出应为：40320"""
#
#
# def func(a):  # n!
#     print(reduce(lambda x, y: x * y, [i for i in range(1, a + 1)]))
#
#
# print("\n输入：", end='')
# a = int(input())
# func(a)
#
# """使用给定的整数n，编写程序以生成包含（i，ixi）的字典，该字典为1到n之间的整数（都包括在内）。然后程序应打印字典。假设向程序提供了以下输入：8\
# 然后，输出应为：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}"""
#
# # 常规方法
# n = int(input("\n我们输入："))
#
# dict_a = {}
# for i in range(1, n + 1):
#     dict_a[i] = i * i
# print(dict_a)
#
# # 字典推导式
#
# n = int(input("字典推导式："))
# dict_b = {i: i * i for i in range(1, n + 1)}
# print(f"dict_b:{dict_b}")
#
# for i in range(3, 0, -1):  # -1
#     print(f"range:{i}")
#
# """斐波那契"""
#
# def fib(x):  # 目标数字是前两个数字之和
#     n, a, b = 0, 0, 1
#     while n < x:
#         print(a)
#         a, b = b, a + b  # 每个循环，均重新赋值：用两个变量去接收'第二个数字'和'前两个数字之和'
#         n += 1
#
#
# """求和: 类似于s=a+aa+aaa+aaaa+aaaaa, 几个数相加由键盘决定，即n"""
#
#
# a = int(input("输入："))  # 数字由“a”构成，共构成n个数字
# n = int(input("输入："))  # 共n个数字
# Tn = 0
# l = []
# for i in range(n):
#     Tn += a
#     a *= 10
#     l.append(Tn)
# print(sum(l))
#
# """ 求前n阶乘的和：1！+2！+3！+4！+5！"""
#
# # 1+1*2+1*2*3+1*2*3*4+1*2*3*4*5 后续数字的结构是：前者*当前遍历次数；
# t = 1  #
# s = 0
# for i in range(1, n+1):
#     t *= i  # 当前循环的阶乘赋值于变量，以便下个循环使用
#     s += t  # 每次循环的值相加
# print(f"结果为：{s}")
#
# """求年龄"""
# s = 10
# for i in range(1, 5):
#     s += 2
# print(s)

"""排序"""
students = [('Bob', -75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(sorted(students, key=lambda t: abs(t[1])))

"""百钱百鸡问题"""
# 根据结果求条件的，肯定要用条件语句做是否满足的判断
l = [int(i) for i in '12345']
print(l)