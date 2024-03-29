# -*- coding=utf-8 -*-
# @Time    : 2022/08/07 14:19
# @Author  : ╰☆H.俠ゞ
# =============================================================
import importlib

import pytest

"""
动态导入和反射
"""

"""
import importlib

a = importlib.import_module("a.a")
a.show()  # Show A
b = importlib.import_module("b.b")
b.show() # Show B
c = importlib.import_module("b.c.c")  # 绝对导入
c.show()  # Show C
d = importlib.import_module(".c.c", package="b")  # 相对导入
d.show()  # Show C


"""


def a():
    """__name__  入口函数，用来区分当前模块是独立运行还是被调用"""
    print(str(__name__).split(".")[-1] + '.yaml')


def b():
    m = importlib.import_module("test__name__")
    func = getattr(m, "test_a")  # getattr(x, 'y') 等价于 x.y
    func()  # 执行函数需加括号 m.test_a()
    print(id(func))
    print(id(func))


def test_c():
    # < import_module > 只能导入包和模块，不能导入模块中的类和方法
    # gc = importlib.import_module(".web_autoTest.demo_import_module.demo_importlib", "Lesson_22")  # 相对导入
    # gc_class = importlib.import_module(".web_autoTest.demo_import_module.demo_importlib", "Lesson_22")  # 相对导入
    gc = importlib.import_module("Lesson_22.web_autoTest.demo_import_module.demo_importlib")  # 绝对导入（路径：工程下第一个包开始）
    getattr(gc, "demo")()

    gc_class = importlib.import_module("Lesson_22.web_autoTest.demo_import_module.demo_importlib")  # 绝对导入（路径：工程下第一个包开始）
    c_demo = getattr(gc_class, "Demo_class")  # 获取模块中的类
    getattr(c_demo(), "demo_c")()  # 【见demo_importlib模块】类方法添加staticmethod静态方法装饰器后，就不用实例化的，直接c_demo.demo_c


if __name__ == "__main__":
    pytest.main()