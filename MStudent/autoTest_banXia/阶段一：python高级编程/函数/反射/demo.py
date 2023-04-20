# -*- coding=utf-8 -*-
# @Time    : 2022/10/23 15:16
# @Author  : ╰☆H.俠ゞ
# =============================================================


class Foo:
    pass


f = Foo()
setattr(f, "x1", "test1")
setattr(f, "y1", "test2")
print(f.__dict__)  # 以字典的形式打印属性
