# @Time  : 2022/02/11 09:57
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================


"""
【测试】

def pytest_runtest_setup(item: "Item") -> None:
    print("hook:setup")

def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("hook:teardown")
"""


def test_demo():
    print("test hook")