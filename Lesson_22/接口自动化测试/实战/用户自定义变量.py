# -*- coding=utf-8 -*-
# @Time    : 2022/09/28 10:48
# @Author  : ╰☆H.俠ゞ
# =============================================================

params = {}


def send():
    pass


def demo(userid):
    params["id"] = userid
    print(params)


def demo1():
    str_a = "abcdefg"
    print(str_a[-5:-3])
    print(str_a[5:3:-1])


if __name__ == '__main__':
    demo(1)
    demo1()