# -*- coding=utf-8 -*-
# @Time    : 2022/09/18 16:48
# @Author  : ╰☆H.俠ゞ
# =============================================================


"""
globals() 是一个字典

"""
import importlib


def test_global_var():
    globals()["a"] = 100  # 先定义全局变量的key和value
    print(f"\n局部打印全局变量a的value值: {globals()['a']}")  # 打印全局变量a的value值


def test_a():
    print(f"全局变量类型为：\n{type(globals())}")
    print(f"\n另外一个函数中打印全局变量a的value值: {globals()['a']}")  # 打印全局变量a的value值


def test_b():
    globals()["tmp"] = 100  # 将下个函数要使用的值声明为全局变量
    return globals()["tmp"]  # 返回全局变量


def test_g():
    # print(f"\n全局：{globals().get('tmp')}")
    print(f"\n全局：{globals()['tmp']}")


def test_b1():
    got_back_result = test_b()  # 获得上一步返回的全局变量
    print(got_back_result)  # 打印上一步返回的全局变量


def test_hasattr():
    # print(str(__name__))
    print(str(__name__).split(".")[-2])
    model_ = importlib.import_module('global_', str(__name__)[-2])
    print(hasattr(model_, "func"))


def test_hasattr1():
    tmp = importlib.import_module("re")
    print(hasattr(tmp, "search"))


def test_import_getattr():
    # gc = importlib.import_module(".web_autoTest.demo_import_module.demo_importlib", "Lesson_22")  # 相对导入
    gc = importlib.import_module("Lesson_22.web_autoTest.demo_import_module.demo_importlib")  # 绝对导入（路径：工程下第一个包开始）
    getattr(gc, "demo")()
