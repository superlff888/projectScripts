# @Time  : 2022/01/18 21:55
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================


# 集合交集

a = {1, 3, 5}
b = {1, 2, 5}
print(a.intersection(b))  # 求交集
print(a & b)  # 求交集

# 并集
c = {2, 8, 10}
print(a.union(b))
print(a.union(b).union(c))
print(a | b)
print(a | b | c)


# 差集
a = {1, 3, 5}
b = {1, 2, 5}
print(a - b)
print(a.difference(b))  # 联想左连接，左边返回不同的{3}
