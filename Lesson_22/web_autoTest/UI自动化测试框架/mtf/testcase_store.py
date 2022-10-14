# -*- coding=utf-8 -*-
# @Time    : 2022/10/08 21:29
# @Author  : ╰☆H.俠ゞ
# =============================================================
import yaml


class TestCaseStore:

    def __init__(self):
        self.test_params = {}
        self.testcase = {}

    def load(self, path):
        with open(path) as f:
            methods = yaml.load(f)
            print(f"type of methods: {type(methods)}")
        for method_name, steps in methods.items():
            step_method = []
            for step in steps:
                step_method.append(step)
            if method_name.startswith("test_"):
                self.test_params[method_name] = step_method
            print(f"test_params: {self.test_params}")
        self.testcase_gen()

    def testcase_gen(self):
        """根据params生成多个testcase"""

        self.testcase = self.test_params
        print(self.testcase)
        print(type(self.testcase))