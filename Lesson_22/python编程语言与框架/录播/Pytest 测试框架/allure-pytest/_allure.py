# @Time  : 2022/02/09 19:26
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
str_a = r"23\n456"
print(str_a)
print(r"23\n456")  # 不换行
print("23\n456")  # 换行

a = [1,2,3,4,5]
a.sort(reverse=True)
print(a)
print(a.index(2))

print(a.count(2))

a={}

print(type(a))
a = lambda x: x**2
print(a(3))
print(a)
