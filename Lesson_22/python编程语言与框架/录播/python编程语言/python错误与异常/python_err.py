# @Time  : 2021/1/12 13:18
# @Author    : House Lee
# -*-coding=utf-8-*-
"""
语法错误、逻辑错误（漏掉if场景导致）、系统错误（内存泄漏）
一般是编码问题
"""
num = 1
if num > 1:  #若没冒号”:“，则发生错误
    print("num>1")


