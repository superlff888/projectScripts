# @Time  : 2022/01/19 21:19
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
语法
result = lambda [arg1 [,arg2, arg3,...argn]]: expression

[arg1 [,arg2, arg3,...argn]]:可选，指定要传递的参数列表；
expression：表达式必选，指定一个实现具体功能的表达式
"""

import math

# 常规写法
#
# def circle_area(r):
#     """
#     :param r: 半径
#     :return: 计算的圆面积
#     """
#     result1 = math.pi * r ** 2  # 圆周率
#     return result1
#
#
# print(f'半径为{10}的圆面积为：{circle_area(10)}')

# lambda 表达式
#
# result2 = lambda r: math.pi*r*r  # r为变量；math.pi*r*r为表达式；变量result2不可以省略，
# # 用一个变量result2 接收lambda表达式的return结果，然后用该变量调用该lambda表达式
# print(f'半径为{10}的圆面积为：{result2(10)}')
# r = 10
# print(lambda r: math.pi * r * r)  # 打印的是内存地址
#
# # lambada表达式使用场景 ：指定一个短小的回调函数
#
# # 1、指定规则进行排序
#
# # lambda x: x[1] 返回了列表中每个元组的第二个元素
# book_info = [("Python基础入门", 22.5), ("java零基础入门", 20), ("软件测试入门", 25)]
# print(book_info)
# print("--------------------------------------------------------------------------\n")
#
#
# def l_sort(x):
#     res = x[1]
#     return res
#
#
# print(l_sort(book_info))
# print("--------------------------------------------------------------------------\n")
#
# # 指定规则进行排序
# book_info.sort(key=lambda x: x[1])  # x表示列表中的一个元素,任意定义变量名
# print(book_info)
#
# # 列表数据按字典key的值排序
# students = [
#     {'name': 'TOM', 'age': 20},
#     {'name': 'ROSE', 'age': 19},
#     {'name': 'Jack', 'age': 22}
# ]

# 按name值升序排列列
# students.sort(key=lambda x: x['name'])
# print(students)
#
# # 按name值降序排列列
# students.sort(key=lambda x: x['name'], reverse=True)
# print(students)
#
# # 按age值升序排列列
# students.sort(key=lambda x: x['age'])
# print(students)

# 注意：lambda: 'lambda表达式'  输出的是函数名（内存地址）


# 常用例子
x1 = 2
y1 = 8
result_a = lambda x, y: x + y
print(lambda x, y: x + y(2, 8))

print(f'x+y的结果：{result_a(2, 8)}')

t = lambda: 'lambda表达式'
print(t())  # 输出的是expression
print(t)

# 直接传参
print("\n\n直接传参---------------------------------------------------")
print((lambda a, b: a + b)(1, 2))

# 带判断的lambda
print(f"带判断的lambda: {(lambda a, b: a if a < b else b)(1000, 500)}")


def lam(a, b):
    if a < b:
        return a
    else:
        return b


print(lam(1000, 500))

# 进阶：编写跳转表
L = [lambda x: x ** 2, lambda x: x ** 3, lambda x: x ** 4]

for f in L:  # f = lambda x: x ** 2
    print(f(2))  # 传入参数2

print(L[0](3))

# 结合高阶函数

leaders = {4: "Yang Zhou", 2: "Elon Musk", 3: "Tim Cook", 1: "Warren Buffett"}
print(leaders)
print(leaders.items())  # 转化为items对象

# 转化为dict
leaders = dict(sorted(leaders.items(), key=lambda x: x[0]))  # 按照可迭代对象的key排序，列表中元组下标为0的元素
print(leaders)

# 默认参数

print(f"默认2为参数： {(lambda x=2: x ** 2)()}")

list_sort = [(4, 'Yang Zhou'), (2, 'Elon Musk'), (3, 'Tim Cook'), (1, 'Warren Buffett')]
list_sort.sort(key=lambda x: x[0])
print(list_sort)

"""
【实战】
 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为[0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
【解析】
 比较tuple的方式，是按照里面元素的顺序一个一个比，找到第一个不相等的元素，这个元素的比较结果就是tuple的比较结果。所以当一个正数和一个负数比较的时候，
 是(False, xxx) vs (True, yyy)，那么第一个元素就不相等了，False比较小，所以正数在前面。如果符号相同，那么tuple里的第一个元素就是相等的，那么
 就比较第二个元素，也就是绝对值小的在前面了
【核心】
1、sorted函数中的lambda表达式中x为可迭代对象的元素本身
2、比较条件为lambda表达式的返回值；比较条件有多个时，先比较第一个，再比较第二个条件
"""

foo = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
# 【实际是lambda返回值做比较】 sorted默认是根据可迭代对象的元素大小排序
# 解析：sorted是根据key排序，实际是根据匿名函数的返回值作为排序条件，若返回两个条件，那就先比较第一个条件，再比较第二个条件
# (True,5) VS (False,8) VS (False,0) VS (False,4) VS (False,9) , 注意：False < True
list_result = sorted(foo, key=lambda x: (x < 0, abs(x)), reverse=False)
print(list_result)

print(False < True)  # 输出：True

foo1 = [{"name": "zs", "age": 19}, {"name": "ll", "age": 54}, {"name": "wa", "age": 17}, {"name": "df", "age": 23}]

list_l1 = sorted(foo1, key=lambda x: x["name"])
list_l2 = sorted(foo1, key=lambda x: (x["name"]))
print(list_l1)
print(list_l2)

"""
生成器：
  与列表推导式的区别是：生成器表达式外侧用小括号包裹
"""

_generator = (i for i in range(10))
print(_generator)

