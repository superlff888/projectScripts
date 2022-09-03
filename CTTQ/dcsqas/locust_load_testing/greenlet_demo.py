# -*- coding=utf-8 -*-
# @Time    : 2022/09/02 22:56
# @Author  : ╰☆H.俠ゞ
# =============================================================
import time
from greenlet import greenlet


def coroutine_yie_en():
    for a in english_list:
        print(f"字母{a}")
        cor2.switch()
        time.sleep(0.5)
    return "字母列表遍历完了"


def coroutine_yie_da():
    for a in data_list:
        print(f"数字{a}")
        cor1.switch()
        time.sleep(0.5)
    return "数字列表遍历完了"


def main():
    cor1.switch()


english_list = ['a', 'b', 'c', 'd']
data_list = [x for x in range(5)]
cor1 = greenlet(coroutine_yie_en)
cor2 = greenlet(coroutine_yie_da)

if __name__ == "__main__":
    main()


"""
这里创建了两个greenlet对象:cor1,cor2。分别对应函数coroutine_yie_en，coroutine_yie_da。
使用greenlet的switch()方法进行协程切换。我们先调用cor1.switch()后函数coroutine_yie_en执行，
在这个函数中又调用了cor2.switch，函数coroutine_yie_da执行，这样来回切换执行，当执行到3后调用cor1.swtich，
函数coroutine_yie_en已经执行完了，不再调用cor2.switch，不会输出4。

"""