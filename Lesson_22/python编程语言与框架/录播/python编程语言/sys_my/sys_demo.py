# @Time  : 2022/02/15 10:34
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""

与python解释器交互的桥梁

与python解释器交互的桥梁

与python解释器交互的桥梁

"""


import sys
import time

# help(sys)  # 查看对应模块(sys)的帮助文档
# print(dir(sys))  # 查看对应模块(sys)的属性和方法


"""
常用方法
"""
print("========================================================================================================================================================================\n")

# 1、获取python的当前版本
print(sys.version)
print(sys.version_info)

# # 2、返回操作系统平台名称
print(sys.platform)

# 返回已导入的模块信息
print(sys.modules)
print(sys.modules.keys())  # key
print(sys.modules.get('sys'))  # value


"""
【sys_import_demo.py模块】
import os
import sys

sys.path.append(os.path.abspath(__file__))  # 已将该模块的abspath放到导包的搜索路径列表，该包（即sys_import）在任何模块均可被直接导入
print(sys.path)

def hello():
    print("hello world")
"""
# 3、返回导包的搜索路径列表(供python查找第三方扩展的模块)，这些路径下的包可以在任何模块中直接导入
print(sys.path)
from sys_import import sys_import_demo

sys_import_demo.hello()

# 4、获得系统当前编码
print(sys.getdefaultencoding())
print(type(sys.getdefaultencoding()))

# 5、运行时，退出
if 1 != 1:
    sys.exit("程序正常退出了")  # message也可不传
print('hello')  # 上一步sys.exit()如果执行，程序就退出了，因而不打印“hello”
for i in range(10):
    if i == 8:
        print("程序正常停止了")
        sys.exit("exit......")
    print(f"running{i}...")
    time.sleep(0.5)
