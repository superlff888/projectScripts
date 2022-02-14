# @Time  : 2022/01/22 18:21
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
【常用命令行参数】
    --help
    -x  用例一旦失败(fail/error),就立刻停止运行
    --maxfail=num  用例失败数达到num时，就停止运行
    -m  标记用例
        标记关键词：@pytest.mark.标记词
        用法： -m=标记词 ; -m 标记词; -m "not 标记词"
    -k  指定含有某关键字的测试用例((包含装饰器-m标记的用例、方法名中含有的关键字))
    -v  打印详细日志
    -s  打印输出日志 (一般-vs一般使用)
    --collect-only  (测试平台，pytest自动导入功能)
"""
import sys
import pytest


# def test_1():
#     assert 1 == 1
#
#
# def test_2():
#     assert 1 == 1
#
#
# @pytest.mark.err  # 标记err测试用例 可用-m参数，指定运行标记用例
# def test_3():
#     assert 1 == 2
#
#
# @pytest.mark.skip
# def test_4():
#     assert 1 == 1
#
#
# def test_5():
#     assert 1 == 1
#
#
# def test_6():
#     assert 1 == 1
#
#
# def test_7():
#     assert 1 == 1
#
#
# def test_8():
#     assert 1 == 1


"""
【内置标签】 mark: 跳过(skip)及预期失败(xfail)
    
    skip  始终跳过该测试用例
        解决方法：1、添加装饰器 pytest.mark.skip 或 pytest.mark.skipif
                2、代码中添加跳过代码 pytest.skip(reason) 
            
    skipif  遇到特定情况跳过该测试用例
    xfail  遇到特定情况，产生一个“期望失败”输出

"""


@pytest.mark.str
def test_sys():
    print(sys.platform)
    print(sys.version)
    print(sys.maxsize)


# 特定条件下跳过该用例
@pytest.mark.skip('用例相关需求代码未开发完')
def test_a():
    print("test_a用例相关需求代码未开发完")
    assert 1 == 1


@pytest.mark.skipif(sys.platform == 'win32', reason='can not run on win32')
def test_b():
    # return True
    # return False
    # assert 1 == 1  # 执行方法后，没有返回值；只是一个判断而已
    return 1 == 1  # 执行方法后，有返回值True


@pytest.mark.skipif(sys.maxsize == 9223372036854775807, reason='the size is too big')
def test_bb():
    print(test_b())


@pytest.mark.skipif(sys.version == '3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)]', reason='the version can not used')
def test_cc():
    print(test_b())


# 在代码块中添加跳过代码
def test_c():
    print('start')
    if not test_b():  # 判断方法test_b()执行结果为布尔值false，事实上方法test_b()返回值为True
        pytest.skip("test_b失败,跳过")  # 跳过后，该方法内后面的代码将不再执行
    print("跳过了？")


def test_d():
    assert 1 == 1


@pytest.mark.int
def test_e():
    assert 1 == 1


"""
命令行参数 - 使用缓存状态

--lf (--last-failed)  只重新运行故障
--ff (--failed-first)  先运行故障，再运行其余的测试
"""


"""
【pytest.ini配置文件】
;ini配置文件由三部分构成：节（section），属性（property），注释（comment）
;属性（property）: 标记多个关键词一定要换行，否则pytest会认为它是一个key
;注意：key和value都不加引号
;host=localhost
;port=8888

"""