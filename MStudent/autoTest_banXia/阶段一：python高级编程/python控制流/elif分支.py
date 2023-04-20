# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 14:58
# @Author  : ╰☆H.俠ゞ
# =============================================================
def cook(time):
    if time <= 3:  # 如果满足，下面的分支就不执行了
        print("3")
    elif time <= 5:
        print("5")
    elif time <= 7:
        print("7")


cook(3)
