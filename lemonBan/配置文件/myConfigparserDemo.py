# @Time  : 2021/06/16 11:43
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import configparser  # 操作配置文件的库


conf = configparser.ConfigParser()

conf.read('my.conf', encoding='utf-8')  # 打开my.conf配置文件

print(conf.sections())  #
print(conf.options('name'))  #
print(f"name(section)中的leader(options)为：{conf.get('name', 'leader')}")  # 打印出读取出的leader的value
print(f"name（sections）中的items:{conf.items('name')}")
print(dict(conf.items('name')))  # 当可以转化成字典时，用dict函数可以转化为字典格式
print(conf.get('age', 'leader'))  # str类型
print(conf.getint('age', 'leader'))  # int类型
print(conf.getfloat('age', 'store'))  # float类型
print(conf.getboolean('age', 'print'))  # 布尔类型


