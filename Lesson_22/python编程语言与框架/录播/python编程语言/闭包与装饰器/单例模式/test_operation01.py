# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 11:25
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.python编程语言与框架.录播.python编程语言.闭包与装饰器.单例模式.base_demo import Base


class Test_X:
    def test_x(self):
        a = Base()
        b = Base()
        print(id(a))
        print(id(b))
        print(a == b)
        assert a == b

    def test_y(self):
        c = Base()
        d = Base()
        print(f"实例id为：\n{id(c)}")
        print(id(d))
        print(c == d)
        assert c == d

