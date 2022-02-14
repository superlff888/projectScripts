# @Time  : 2021/06/08 20:38
# @Author    : House Lee
# -*-coding=utf-8-*-
#
# class Test:
#     def __init__(self):  # 设置属性
#         self.name = 'H.lee'
#
#     # 父类有个特性：设置属性的时候会触发__setattr__方法;默认已经继承了父类object()
#     def __setattr__(self, key, value):  # 通过init方法设置属性的时候该__setattr__方法会被触发，前提通过super()调用父类__setattr__方法
#         print("这是一个__setattr__属性，设置属性的时候会触发")
#         super().__setattr__(key, value)  # 一定要调用父类（object()）的方法，否则不会设置属性
#         print(key, value)
#
#     def __delattr__(self, item):
#         print("删除属性的时候会触发")
#
#
# t = Test()
# # print(t.name)


"""
单元测试
    就是对单个模块、单个类、单个函数进行测试，一般是由开发做的；
测试分类
    按阶段分为：单元测试，集成测试，系统测试，验收测试
"""
