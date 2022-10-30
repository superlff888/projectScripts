# -*- coding=utf-8 -*-
# @Time    : 2022/10/30 15:34
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest


class TestHello:
    def test_demo1(self):
        with pytest.raises(ValueError) as exc_info:
            raise ValueError("抛出异常！")  # 发生异常，异常代码后面的代码就不会执行
