# @Time  : 2021/1/12 13:18
# @Author    : House Lee
# -*-coding=utf-8-*-

"""
注意错误与异常的区别:
    异常可以被捕获和处理；
    错误一般都是编码错误，逻辑错误，系统，一般可以避免的
"""
# 异常处理，提高代码运行容错性
'''
# 除零异常(ZeroDivisionError)
def div(a, b):
    return a / b


print(div(1, 0))
'''

# --------------------------------------------------------
"""
异常类型（https://docs.python.org/3/library/exceptions.html）
"""


# # 名称异常（NameError）
#
# num = 1        num不同于nam
# if nam > 1:
#     print("num>1")

# #  索引异常(IndexError)
# list_a = [1, 2, 3, 5, 6]
# print(list_a[5])


# #  键异常(KeyError¶)
# dict_a ={"name":"lily"}
# print(dict_a["age"])


# #  值异常(KeyError¶)
# num = input("请输入一个值： ")
# print(int(num))


# 断言异常(AssertionError)
#
# 属性异常(AttributeError)
#
# 类型异常(TypeError)
# 关联的值是一个字符串，提供有关类型不匹配的详细信息
# ----------------------------------------------------------------------------
#  【异常处理】
##  方法一：
# def div(a, b):
#     if b != 0:
#         return a / b
#     else:
#         print("除数不可以为零！")
#         return 0
#
#
# print(div(1, 0))


##  方法二：

# def div(a, b):
#     return a / b
#
#
# try:
#     print(div(1, 0))
# except:  # 无法抛出异常
#     print("这里有异常")

# ------------------------------------------------------------------------

def div(a, b):
    return a / b


f = open('data.txt')

try:                      # 此处为执行的语句,发生异常后，try中剩下的代码就不执行，然后通过except来处理异常（打印或主动抛出），最后执行finally语句
    # print(div(1, 0))        # 除数为0异常
    list1 = [1, 2, 3, 5]
    print(list1[1])         # 索引异常
    assert list1[1] == 3, f'index为1的元素预期为{list1[1]},实际为2'  # AssertionError: index为1的元素预期为2,实际为2
    print(f.readlines())    # 文件读取(f = open('data.txt'))
# except ZeroDivisionError as e1:
#     print(e1)
# except IndexError as e2:     # 一般常用
#     print(e2)
except Exception as e:  # 此处捕获异常：只捕获第一个异常
    # print(f"此处的异常为：'{e}'")
    raise Exception
    # raise e
    # raise Exception("索引异常")  # Exception: 索引异常

else:
    print("没有发生异常")

finally:  # finally 最终都会被执行
    print(f"finally：已经抛出的异常")
    f.close()  # 关闭文件

"""
主动抛出异常->开发时，有些业务逻辑不符合需求时，就会主动抛出异常
"""

# def set_age(num):
#     if num < 0 or num > 100:
#         raise ValueError(f"输入的值（{num}）错误")
#     else:
#         print(f"设置的年龄为：{num}")
#
#
# set_age(2000)

"""
自定义异常：
    自定义一个异常种类
"""

# class MyError(Exception):  # 自定义一个异常,如何取调用该异常呢
#     def __init__(self, msg):
#         print(f"This is a Exception : {msg}.")
#
#
# def set_age(num):
#     if num < 1 or num > 100:
#         raise MyError(f"错误值为：{num}")
#     # raise MyError：抛出自定义异常，既是调用了MyError类构造方法；【'错误值为 : -50'】就是MyError构造方法中的参数（debug调试下即可明白）
#     else:
#         print(f"There are no Exception;设置的年龄为 : {num}")
#
#
# set_age(-50)

"""
除零异常、名称异常、索引异常、键异常、值异常、属性异常
"""
