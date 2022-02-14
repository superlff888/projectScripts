# @Time  : 2021/06/09 00:09
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================

"""
按照__new__(cls)方法定义的规则初始化一个类对象，所以此时的logger就是my_log
"""
from lemonBan.apiTest.lib.logs.loggerMy import MyLogging


print("开始日志")
logger = MyLogging("DEBUG", './myLog.log')  # 调用__new__方法
logger.error("这是一个error日志")
