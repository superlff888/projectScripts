# -*- coding=utf-8 -*-
# @Time    : 2022/10/16 15:03
# @Author  : ╰☆H.俠ゞ
# =============================================================

SUM = 1


def get_add_sum(sum=0):
    def add_num(num):
        nonlocal sum  # 用global共享全局变量SUM，nonlocal共享"外部函数"的sum局部变量；切记不可 nonlocal SUM
        sum += num
        print(f"add_num {sum}")
        print(f"get_add_sum {sum}")
        return sum
    return add_num


add = get_add_sum(0)
print(type(add))  # 返回add_num方法的内存地址
print(add(10))  # 调用add_num，输出：10
print(add(20))  # 调用add_num，输出：30
print(add(30))  # 调用add_num，输出：60

"""global共享全局变量；nonlocal共享类变量"""
"""
闭包：
1、闭包的内部函数中，可以引用外部作用域的变量参数
2、闭包无法修改外部函数的局部变量，除非使用nonlocal关键字
3、闭包可以保存当前的运行环境
"""