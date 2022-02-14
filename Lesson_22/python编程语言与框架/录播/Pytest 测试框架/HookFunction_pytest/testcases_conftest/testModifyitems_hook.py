# @Time  : 2022/02/11 10:29
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import pytest


"""
修改默认编码，需要处理两点：
1、测试用例名字
2、测试用例的路径
"""


@pytest.mark.parametrize('name', ['哈利波特', '赫敏'])
def test_mh(name):
    print(f'name: {name}')
