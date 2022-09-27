# -*- coding=utf-8 -*-
# @Time    : 2022/09/26 14:08
# @Author  : ╰☆H.俠ゞ
# =============================================================

# print((lambda x: x * 2)(2))
# print(list(map((lambda x: x ** 2), [1, 2, 3])))
# print((lambda x, y: x * y)(2, 3))

# a = {"a": 1, "b": 2, "c": 3}
#
#
# for k, v in a.items():
#     print(f"k, v 为：{(k, v)[0]}")


# while True:
#     x = int(input("输入数字："))
#     if x == 66:
#         print("猜对了！")
#         break


# n = 1
#
# while n <= 3:
#     input("用户名：")
#     input("密码：")
#     n += 1
#     if n == 4:
#         print("密码错误")
import random

name = "testfan"
# print(name)
# print(name[:-1])
# print(name[::-1])


dict_a = {'age': 18, 'status': True, 'name': '极光'}

for item in dict_a.items():
    print(item[0], item[1])
    print(item)
print("====================================")
for k, v in dict_a.items():
    print(k, v)

print("====================================")
a = [k for k in dict_a.items()]
print(a)

a = [8, 1, 2, 1, 3]
# a.insert(0, 1)
# print(a)
# print(a.remove(1))
# print(a)
a.sort(reverse=True)
print(a)
b = ["dcdsfc", "qwcd", "qwdvfbgh"]
b.sort(key=len, reverse=True)  # 键函数
print(b)


# 字典推导式

dict_b = {'age': 18, 'status': True, 'name': '极光'}
print(dict_b.items())
print({k: v for k, v in dict_b.items()})

items = [('age', 18), ('status', True), ('name', '极光')]
b = {k: v for k, v in items}
print(b)
print(b.get("age"))
print(b.keys())
print(b.popitem())
print(b.pop("age"))
print(b)

