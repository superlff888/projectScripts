# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 11:25
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.python编程语言与框架.录播.python编程语言.闭包与装饰器.单例模式.base_demo import Base
from Lesson_22.python编程语言与框架.录播.python编程语言.闭包与装饰器.单例模式.operation2 import Demo_y


class Demo_x:
    def demo_x1(self):
        Base().sleep()
        print(f"demo_x1:  {id(Base())}")

    def demo_x2(self):
        Base().eat()
        print(f"demo_x2:  {id(Base())}")
        return Demo_y()