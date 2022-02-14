# @Time  : 2021/06/09 00:09
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================


"""
按照__new__(cls)方法定义的规则初始化一个类对象，所以此时的logger就是my_log
"""
from Lesson_22.python编程语言与框架.录播.python编程语言.logs.封装日志公共函数.loggerMy import MyLogging

logger = MyLogging('DEBUG', 'myLog.log')
logger.info("这是一个info日志")
