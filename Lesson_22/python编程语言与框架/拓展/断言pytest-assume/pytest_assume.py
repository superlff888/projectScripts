# @Time  : 2022/02/12 12:41
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import pytest

"""
1、对比原生assert和pytest-assume的测试用例
"""


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assert(x, y):
    # 逗号后面为断言消息AssertionError: index为1的元素预期为1,实际为0
    assert x == y, f'预期为{x},实际为{y}'  # 如果这个断言失败，则后续都不会执行
    assert True
    assert False


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_pytest_assume(x, y):
    pytest.assume(x == y)  # 即使这个断言失败，后续仍旧执行
    pytest.assume(True)
    pytest.assume(False)


"""
2、通过上下文管理器with使用pytest-assume
"""


# @pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
# def test_simple_assume2(x, y):
#     # 使用上下文管理器的好处是不用显示去try和finally捕获异常，建议使用这种写法，简洁有效。
#     with assume: assert x == y
#     print("\n=========继续执行==============\n")
#     with assume: assert True
#     with assume: assert False


"""
3、上下文管理器里面包含多个断言，则只有第一个会被执行
"""


@pytest.mark.parametrize(('x', 'y'), [(1, 1), (1, 0), (0, 1)])
def test_simple_assume3(x, y):
    # 使用上下文管理器的好处是不用显示去try和finally捕获异常，建议使用这种写法，简洁有效。
    with pytest.assume:
        # 若断言失败，则后续断言停止被执行！
        assert x == y
        print("\n=============================================================================\n下面的断言不应该被执行\n")
        assert True
        assert False
