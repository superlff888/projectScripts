# -*- coding=utf-8 -*-
# @Time    : 2023/01/31 21:50
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
适用于web和app
"""


import pytest


@pytest.fixture(scope="module", autouse=True)
def record_video():
    command = "scrcpy --record tmp.mp4"
