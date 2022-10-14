# -*- coding=utf-8 -*-
# @Time    : 2022/10/08 21:28
# @Author  : ╰☆H.俠ゞ
# =============================================================

# from context_base import ContextBase
from Lesson_22.web_autoTest.UI自动化测试框架.mtf.context_base import ContextBase


class TestCase(ContextBase):
    def __init__(self, steps, context):
        self.steps = steps
        self._context = context
        # self.set_context(context)

    def run_steps(self):
        # self.get_context()应该是类Context()实例context
        # 突破点在run_steps_by_testcase方法中TestCase(steps, self)第二个传参“self”
        self.get_context().run_steps(self.steps)