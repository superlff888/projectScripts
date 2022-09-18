# -*- coding=utf-8 -*-
# @Time    : 2022/09/18 17:07
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""加上global声明看下："""

list1 = [1, 2, 3, 4, 5]
str1 = 'hello world!'


def func():
    global list1, str1  # 将函数内变量声明为外部已经定义好的全局变量
    list1 = [6, 7, 8, 9, 10]  # 将全局变量重新赋值
    str1 = '你好，世界！'  # 将全局变量重新赋值
    print(list1)
    print(str1)


func()
print(list1)
