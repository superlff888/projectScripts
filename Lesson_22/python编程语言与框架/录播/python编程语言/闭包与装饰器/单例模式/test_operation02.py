# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 15:26
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.python编程语言与框架.录播.python编程语言.闭包与装饰器.单例模式 import singleon
from Lesson_22.python编程语言与框架.录播.python编程语言.闭包与装饰器.单例模式.operation1 import Demo_x


class Test_operation:

    def setup_class(self):
        self.dm = Demo_x()

    def test_a(self):
        self.dm.demo_x1()

    def test_instance1(self):
        print(singleon._instance)

    def test_b(self):
        self.dm.demo_x2().demo_y2()

    def test_instance2(self):
        print(singleon._instance)


"""
【单例模式】装饰器加强后，实例本身仅会实例一次，故名单例化;
         operation中打印的id是一样的
"""
