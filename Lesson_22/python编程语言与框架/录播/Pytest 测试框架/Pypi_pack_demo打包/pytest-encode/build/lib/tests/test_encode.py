# @Time  : 2022/02/12 00:12
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import pytest


@pytest.mark.parametrize('name', ['哈利波特', '赫敏'])
def test_mh(name):
    print(f'name: {name}')
