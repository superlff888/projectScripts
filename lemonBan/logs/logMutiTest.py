# @Time  : 2021/06/09 08:33
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================


"""
此处logger为类对象，并不是收集器
"""
from lemonBan.logs.loggerMutiLevel import MyLogging

logger = MyLogging('INFO')
# self就是实例本身，即上面的“logger”; logger._debug是一个DEBUG级别的收集器
logger._info.info("\n\nparam: name, age\n\nSQL: select * from org_person_a where person_code like %810%;")
