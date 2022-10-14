# -*- coding=utf-8 -*-
# @Time    : 2022/10/08 21:22
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from Lesson_22.web_autoTest.UI自动化测试框架.mtf.context import Context


class TestMain:
    context = Context()
    # 生成测试用例testcase，以
    context.load("./tmp.yaml")

    @pytest.mark.parametrize("testcase", context.store.testcase.values(), ids=context.store.testcase.keys())
    def test_main(self, testcase):
        self.context.run_steps_by_testcase(testcase)
