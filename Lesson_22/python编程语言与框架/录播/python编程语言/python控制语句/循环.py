# @Time  : 2022/01/17 22:33
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import random

"""
for in 循环
"""
# 前闭后开原则
import random

range(101)  # 0~100
range(1, 101)  # 1~100
range(1, 100, 2)  # 1~99的奇书序列
#
# for i in range(1, 100, 2):
#     print(f"产生的奇数序列：{i}")
#
# print("--------------------------------------------------------------------------")
#
#
# # 跳出整个循环break
# for i in range(0, 100, 2):
#     print(f"产生的偶数序列：{i}")
#     if i == 50:
#         print("生产结束")
#         break

# 跳出单次循环
list_a = [1, 2, 3, 4, 5]
for i in list_a:

    if i == 3:
        print(f"跳出第{i}次循环")
        continue
    print(f"获取列表元素：{i}")


print("------------------------------------------------------------")


'''
while 循环
'''

a = 1
while a < 6:
    print(a)
    a += 1
    if a == 3:  # 满足业务条件
        print("跳出循环")
        break  # 跳出循环


b = 1
while b < 6:
    if b == 3:
        b += 2.1
        continue  # 跳出该次循环，不再往下执行while循环体
    b += 1
    print(b)
print(b)


# 获取0~100之和
print(sum(range(101)))
# 获取获取0~100之间的偶数之和
print(f"sum函数获得偶数之和：{sum(range(0, 101, 2))}")

sum_ = 0
for i in range(0, 101, 2):
    sum_ += i
print(f"for循环偶数之和：{sum_}")

# 随机取数

random_num = random.randint(1, 10)
print(f"获得的随机数：{random_num}")
