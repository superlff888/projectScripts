# @Time  : 2022/02/11 21:59
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================


def test_addoption(cmdoption):  # 传入fixture函数
    print("\n")
    print(cmdoption)  # fixture函数执行时不需要加()
    a, b = cmdoption
    print(a, b)

