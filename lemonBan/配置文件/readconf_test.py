# @Time  : 2022/02/12 16:37
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
from lemonBan.配置文件.readConfig import ReadConfig

conf = ReadConfig('./my.conf')

print(conf.get('age', 'leader'))  # str类型
print(conf.sections())