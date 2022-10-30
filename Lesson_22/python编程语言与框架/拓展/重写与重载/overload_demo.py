# @Time  : 2022/02/13 13:25
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

from typing import overload

"""
加了@overload装饰器的方法都会被一个不加装饰器的方法覆盖掉,改变的是参数类型
"""


@overload
def demo(name: str) -> str:
    print(f"str:{name}")


@overload
def demo(name: float) -> str:
    print(f"float:{name}")


@overload
def demo(name: int, age: str) -> str:
    pass


@overload
def demo(name: int, age: dict) -> str:
    pass


@overload
def demo(name: int, age: list, weigh: int):  # 此处的weigh因为没有overload，所以只有int一种入参
    return f"hello {name},我{age}了,体重{weigh}"


print(demo(10, "18"))


