# -*- coding=utf-8 -*-
# @Time    : 2022/08/07 14:57
# @Author  : ╰☆H.俠ゞ
# =============================================================
# from Lesson_22.web_autoTest.mtbDriver import mbtdriver


def test_a():
    """__name__  入口函数，用来区分当前模块是独立运行还是被调用"""
    # str(__name__) --> Lesson_22.web_autoTest.mtbDriver.test__name__
    print(str(__name__))  # 入口就是当前py文件 --> mtbDriver.test
    print(str(__name__).split(".")[-1]+'.yaml')  # Lesson_22.web_autoTest.mtbDriver.test__name__
    dict_a = {"x": 1}
    print(dict_a.items())
    a = 'test_a'
    a.startswith("test_")
    globals()["para"] = 100

    # para1 = 100
    return globals()["para"]


# def test2(param1=None):
#     para_g = test_a()
#     # print(globals()["para"])
#     print(para_g)
#     print(param1)  # fixture 'param1' not found
#
#
# def test3():
#     a = 10
#     print(eval("a"))  # must be a string
#     if 1 < 2:
#         pass
#     print("over")
#
#
# def test_demo():
#     try:
#         2/0
#     except ZeroDivisionError as e:
#         raise e
#     print("over: 不应该走这块代码")