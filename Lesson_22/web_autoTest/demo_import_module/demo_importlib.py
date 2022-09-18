# -*- coding=utf-8 -*-
# @Time    : 2022/09/18 20:17
# @Author  : ╰☆H.俠ゞ
# =============================================================


def demo():
    print("动态导入测试")


class Demo_class:
    @staticmethod
    def demo_c():  # 添加静态方法装饰器后，调用该方法时就不用实例化，即 Demo_class()
        print("这是类中的方法")