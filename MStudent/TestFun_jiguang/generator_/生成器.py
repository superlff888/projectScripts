# -*- coding=utf-8 -*-
# @Time    : 2023/04/07 00:17
# @Author  : ╰☆H.俠ゞ
# =============================================================


def create_big_num(max_num):
    """边执行边造数据,提高性能；减少内存使用"""
    num = 0
    while True:
        yield num
        if num == max_num:
            return
        num += 1


a = create_big_num(10)
# print(next(a))
# print(next(a))
# print(next(a))


"""支持for循环"""

for i in a:
    print(i)