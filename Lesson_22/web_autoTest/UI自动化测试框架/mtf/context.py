# -*- coding=utf-8 -*-
# @Time    : 2022/10/08 21:24
# @Author  : ╰☆H.俠ゞ
# =============================================================

from Lesson_22.web_autoTest.UI自动化测试框架.mtf.testcase import TestCase
from Lesson_22.web_autoTest.UI自动化测试框架.mtf.testcase_store import TestCaseStore


class Context:
    def __init__(self):
        self.store = TestCaseStore()
        self.testcase = None
        self._return_value = None

    def load(self, file_name):
        self.store.load(file_name)

    def run_steps_by_testcase(self, steps):
        # self
        self.testcase = TestCase(steps, self)
        self.testcase.run_steps()

    def run_steps(self, steps):
        for Step in steps:  # 可以理解为Step在Context内存地址中
            # Step().set_context()
            Step.set_context(self)  # step肯定是Step()实例，由于继承了ContextBase，所以拥有set_context()方法
            self._return_value = Step.run()

    def return_value(self):
        return self._return_value

