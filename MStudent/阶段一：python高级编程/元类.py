# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 16:12
# @Author  : ╰☆H.俠ゞ
# =============================================================


def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建Hello class
h = Hello()
h.hello()


"""
要创建一个class对象，type()函数依次传入3个参数：
1、class的名称；
2、继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
3、class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。
"""