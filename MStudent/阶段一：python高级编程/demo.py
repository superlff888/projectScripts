# -*- coding=utf-8 -*-
# @Time    : 2022/09/26 14:08
# @Author  : ╰☆H.俠ゞ
# =============================================================

# print((lambda x: x * 2)(2))
# print(list(map((lambda x: x ** 2), [1, 2, 3])))
# print((lambda x, y: x * y)(2, 3))

a = {"a": 1, "b": 2, "c": 3}


for k, v in a.items():
    print(f"k, v 为：{(k, v)[0]}")