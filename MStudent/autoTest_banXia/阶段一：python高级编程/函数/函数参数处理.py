# -*- coding=utf-8 -*-
# @Time    : 2022/10/16 11:48
# @Author  : ╰☆H.俠ゞ
# =============================================================


def do_something(*args, a=None, **kwargs):
    n = len(args)
    print(f"长度：{n}")
    if n >= 1:
        for i in range(n):
            print(args[i])
    else:
        pass
    print(f"a: {a, }, kwargs:{kwargs}, 类型为{type(kwargs)}")


do_something(1, 2, 3, 5, a=2, b=3)
# do_something()  # 元组和字典可接收空