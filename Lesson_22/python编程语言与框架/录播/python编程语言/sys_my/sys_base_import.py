# -*- coding=utf-8 -*-
# @Time    : 2022/10/15 21:27
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import sys


# 获取当前文件路径
# print(os.path.dirname(__file__))

p = r"D:\Develop\git_pub_repositories\projectScripts\Lesson_22\python编程语言与框架\录播\python编程语言\sys_my"
# 添加环境变量，即导包路径
# sys.path.append(os.path.dirname(__file__) + "../sys_import")
# print(sys.path)
print(f"当前文件绝对路径：{os.path.abspath(__file__)}")
print(f"【sys_import】：{os.path.abspath(os.path.dirname(__file__) + './sys_import')}")
print(f"【字符串拼接时，注意路径要正确】：{os.path.dirname(os.path.dirname(__file__) + '/sys_import')}")
print(f"【获得当前文件所在目录的上一层目录】：{os.path.dirname(os.path.dirname(__file__))}")
# print(f"【../】{os.path.abspath(os.path.dirname(__file__) + './../')}")  # 字符串拼接，然后才有os.path.abspath方法
# print(f"【p + '../'】{os.path.abspath(p + '/../')}")
# print(os.path.abspath(os.path.dirname(__file__) + "/../../"))
print(os.path.abspath(os.path.dirname(__file__) + "/"))
# print(os.path.abspath(r"D:\Develop\git_pub_repositories\hogwartsCODE\pythonBattle_pytest\src\../demo"))
# 删除导报环境变量
# sys.path.remove(os.path.dirname(__file__))
# print(sys.path)
# from sys_import.sys_import_demo import hello


# print(dir(sys))