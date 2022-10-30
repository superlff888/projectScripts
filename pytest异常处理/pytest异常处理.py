# @Time  : 2022/01/23 10:35
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
常用的异常处理方法
(1) try...except
(2) pytest.raises()
(3)发生异常，raise后面同级代码就不执行了
"""

import pytest


def div(a, b):
    return int(a / b)


@pytest.mark.parametrize('a, b, c',
                         [(10, 2, 5), (0, 2, 0), (2, 0, pytest.raises((ArithmeticError, ZeroDivisionError, ValueError)))],
                         ids=["整除", "被除数为0", "除数为0"])
def test_div(a, b, c):

    if b == 0:
        with c as exc_info:  # 捕获异常
            raise ArithmeticError("算数异常,除数不可以为0")  # 抛出捕获的异常; 抛出的异常类中init构造方法中要传一个消息参数：msg,自定义该信息
        print(f"exc_info.value -->{type(exc_info.value.args)}")
        print(f"exc_info -->{type(exc_info)}")
        assert exc_info.value.args[0] == "算数异常,除数不可以为0"  # exc_info.value.args是一个元组;
        print("执行了")
    else:
        print(f'计算后的结果为：{a / b}')
        assert a / b == c

