# @Time  : 2022/02/13 13:25
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
from typing import overload


# @overload
# def test(name: str) -> str:
#     pass
#
#
# @overload
# def test(name: float) -> str:
#     pass
#
#
# @overload
# def test(name: int, age: int) -> str:
#     ...


from typing import overload


@overload
def test(name: str) -> str:
    pass


@overload
def test(name: float) -> str:
    pass


@overload
def test(name: int, age: int) -> str:
    pass


def test(name, age=18):
    return f"hello {name}"


print(test("10.0"))

