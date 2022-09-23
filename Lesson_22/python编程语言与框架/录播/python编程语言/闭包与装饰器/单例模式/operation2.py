# -*- coding=utf-8 -*-
# @Time    : 2022/09/23 15:19
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.python编程语言与框架.录播.python编程语言.闭包与装饰器.单例模式.base_demo import Base


class Demo_y:
    def demo_y2(self):
        print("跳转页面")
        Base().jump()
        print(f"demo_y2:  {id(Base())}")


