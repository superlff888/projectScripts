# -*- coding=utf-8 -*-
# @Time    : 2022/10/23 14:54
# @Author  : ╰☆H.俠ゞ
# =============================================================

from functools import singledispatch
"""singledispatch 实现重载"""

@singledispatch  # 单一调度
def fun(arg):
    print(arg)


@fun.register
def _(arg: int):
    print(f'arg is int: {arg}')


@fun.register
def _(arg: list):
    print(f'arg is list: {arg}')


@fun.register
def _(arg: str):
    print(f'arg is str: {arg}')


if __name__ == '__main__':
    fun([1, 2, 3])
    fun(1)
    fun('str')
