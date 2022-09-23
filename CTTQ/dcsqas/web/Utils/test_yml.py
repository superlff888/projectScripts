# -*- coding=utf-8 -*-
# @Time    : 2022/09/22 14:20
# @Author  : ╰☆H.俠ゞ
# =============================================================
import unittest

import pytest


class Test_yml(unittest.TestCase):

    def test_assert(self):
        # self.assertEqual(1, 2)
        # self.assertEqual(1, 3)
        pytest.assume(1 == 2)
        pytest.assume(1 == 3)