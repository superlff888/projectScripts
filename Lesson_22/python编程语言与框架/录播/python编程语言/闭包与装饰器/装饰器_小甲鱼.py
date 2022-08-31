# -*- coding=utf-8 -*-
# @Time    : 2022/08/31 14:37
# @Author  : ╰☆H.俠ゞ
# =============================================================


""""""

import time


def myFunc():
    print("程序正在运行")


def time_master(func):
    print("程序开始运行……")
    start = time.time()
    func()
    stop = time.time()
    print(f"程序已经运行了{(stop-start):2f}秒")


time_master(myFunc)