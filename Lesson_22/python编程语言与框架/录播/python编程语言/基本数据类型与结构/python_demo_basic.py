# @Time  : 2021/1/12 13:18
# @Author    : House Lee
# -*-coding=utf-8-*-

"""
关键字传参
在调用函数的时候，使用k=v的方式进行传参；在函数调用/定义中，关键字传参必须跟随在位置参数的后面。
"""
#
#
# def demo_1(a, b, c):
#     """
#     #函数demo的作用
#     :param a:
#     :param b:
#     :param c:
#     :return:
#     """
#     # ctrl+d 快速复制一行代码
#     print("这是一个参数a", a)
#     print("这是一个参数b", b)
#     print("这是一个参数c", c)
#     print("")
#     print()
#     return
#
#
# demo_1(c=1, a=2, b=3)
# demo_1(10, c=20, b=15)  ##位置传参为第一执行顺序,所以传参时必须对应函数参数位置

'''
默认参数在定义函数的时候试用k=v的形式定义；
调用函数时，若没有传参，则使用默认参数；若传参，则使用传递的参数。
'''


# def demo_2(a=2):
#     print(a)


# demo_2()


"""
Lambda表达式>>>python函数
lambda x, y:x+y
lambda作为一个表达式，定义了一个匿名函数，上例的代码【x，y为入口参数，x+y为函数体】。在这里lambda简化了函数定义的书写形式
可以用lambda关键字创建一个小的匿名函数；lambda的主体是一个表达式，而不是一个代码块；仅仅能在lambda表达式中封装有限的逻辑进去。
"""

'''
def demo_3(x):
    return x * 2
'''

# demo_3 = lambda x, y: x * y
# print(demo_3(2, 3))
# # 拓展
# print(f"结果是{(lambda x: x + 1)(2)}")  # 这里的2是实参

"""
三目运算（条件控制语句）->if
"""
# # a = int(input("请输入数字： "))
# # b = int(input("请输入数字： "))
# a = 20
# b = 10
# num = a + b if a > b else a - b
# print(num)

"""
列表推导式->for
"""
# list_a = [i ** 2 for i in range(1, 4)]
# print(list_a)
# list_b = [i ** 2 for i in range(1, 4) if i != 1]  # 先执行控制语句(for循环套if语句)，再执行运算
# print(list_b)
# list_c = [i * j for i in range(1, 4) for j in range(1, 4)]  # 嵌套循环语句
# print(list_c)
# list_d = [i ** j for i in range(1, 5) for j in range(1, 6)]  # 每个i要匹配5个j
# print(list_d)
# e = [i for i in 'qwudhvcfvfbvgdhkfraaaaaaaaaaaaa']
# print(f"list是{e}")
# F = set(e)  # z转化成集合后，自动去重
# print(f"转化成的集合为{F}")
# """
# 字典推导式->for
# """
# dict_A = {i: i ** 2 for i in range(1, 3)}

"""
集合推导式->for
"""
# a = {i for i in 'qwudhvcfvfbvgdhkfraaaaaaaaaaaaa'}
# print("集合为%s" % a)
# print(f"集合是{a}")
# print(set(a))  # 集合有自动去重的作用
# b = a.union()  # 取并集
# a = {i for i in 'qwudhvcfvfbvgdhkfraaaaaaaaaaaaa'}
# print(f"a集合为{a}")
# c = {"周杰伦", "黄圣依"}
# g = a.union(c)
# print(f"a、c的并集是{g}")
# v = a.union(["kobe", "Jordan", "aaa"])  # 取并集
# d = a.union({"kobe", "Jordan", "aaa", "111111111"})  # 取并集
# print(f"两个集合的并集为: {b}和{d}")

# print("去重后的集合为: %s" % b)
# print(f"去重后的集合为: {b}")

"""
字典
"""
# dict_a = {"a": 1, "b": 2, "c": 3}
# print(dict_a["a"])
# print(dict_a.keys())
# print(set(dict_a.keys()))
# print(dict_a.values())
