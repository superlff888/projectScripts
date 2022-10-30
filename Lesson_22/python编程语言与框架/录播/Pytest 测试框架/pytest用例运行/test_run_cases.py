# -*- coding=utf-8 -*-
# @Time    : 2022/10/24 20:32
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os

import pytest


def setup_module():
    print("begin_module")


def teardown():
    print("stop_module")


def setup_function():
    print("begin_func")


def test_boole():
    assert 1 == 1


def teardown_function():
    print("stop_func")


class TestDemo:
    def setup(self):
        print("begin")

    @pytest.mark.skipif('1 == 1', reason="这里1==1是代码跳过的原因")
    def test_1(self):
        pass

    @pytest.mark.skip("这里是代码跳过的原因")
    def test_demo_1(self):
        assert 2

    # @pytest.mark.xfail
    def test_demo_2(self):
        assert 2 == 1


if __name__ == "__main__":
    # os.system("pytest -sv")
    pytest.main(["test_run_cases.py", "-sv"])
