# -*- coding=utf-8 -*-
# @Time    : 2022/10/08 23:09
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.web_autoTest.UI自动化测试框架.mtf.testcase_store import TestCaseStore


class TestTmp:

    def test_demo(self):
        self.testCaseStore = TestCaseStore()
        self.testCaseStore.load("./tmp.yaml")


