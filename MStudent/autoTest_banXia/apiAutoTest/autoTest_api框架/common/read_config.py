# @Time  : 2022/02/10 17:30
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import configparser
from functools import singledispatchmethod

from autoTest_banXia.apiAutoTest.autoTest_api框架.setting import DIR_NAME

"""
封装的原则：
    写死的固定数据（变量），可以封装成类属性，如 配置文件名 config.ini，来控制其他配置文件
    实现某个功能的代码封装成方法，
    在各个方法中都要用到的数据，抽离出来作为实实例属性
封装前，读配置文件数据三部曲：
    conf = configparser.Configparser()  # 实例化
    conf.read('config.ini', encoding='utf8')  # 实例化配置文件解析器，打开配置文件，然后才可以调用get等方法获取想要的数据
    conf.get(section, option)  # 获取options数据
"""
##
"""
    conf = configparser.Configparser()  # 实例化
    conf.read('config.ini', encoding='utf8')  # 打开配置文件，然后才可以调用get等方法获取想要的数据
    conf.get(section, option)  # 获取options数据
"""


class ReadConfig(configparser.ConfigParser):
    section = {}
    option = {}

    def __init__(self, filepath, encoding='utf8'):
        """
        ::filepath : 相对路径（入参为项目下的路径，参照setting.py路径），如：./conf/*.*

        [function] self.read(DIR_NAME+filepath, encoding) 读取配置文件的内容到配置文件解析器对象,通过解析器调用所属方法，操作配置文件

        """
        # 执行完此步骤，就可调用父类的成员属性，相当于把父类的__init__方法和成员属性继承过来了；
        super().__init__()
        # 通过子类实例对象（self，即conf）调用父类的read方法（继承），加载配置文件(可进一步做参数化)
        self.value = None
        self.con_par = self.read(DIR_NAME + filepath, encoding)

    @singledispatchmethod
    def configParser(self, args):
        raise NotImplementedError("Cannot negate a")

    @configParser.register
    def _(self, args: list):
        sector, item = args
        try:
            self.value = self.section[sector][item]
        except Exception as e:  # KeyError: 'logging'  字典中没有该key
            # print(Exception(f"KeyError: 字典中没有该键:{e},可添加到该字典中"))
            self.value = self.get(sector, item)
            self.option[item] = self.value
            self.section[sector] = self.option
        finally:
            return self.value

    @configParser.register
    def _(self, args: tuple) -> dict:
        sector, item = args
        try:
            # 可能会调两次该方法；第二次调用时字典中就有值了，因而没有KeyError
            self.value = self.section[sector][item]
        except Exception as e:  # KeyError: 'logging'  字典中没有该key
            # print(Exception(f"KeyError: 字典中没有该键:{e},可添加到该字典中"))
            value = self.get(sector, item)
            self.option[item] = value
            self.section[sector] = self.option
        finally:
            return self.section


conf_parser_obj = ReadConfig("./conf/setting.ini")

if __name__ == '__main__':
    conf_parser_obj = ReadConfig("./conf/setting.ini")
    print(conf_parser_obj.configParser(('logging', 'level')))
    print(conf_parser_obj.configParser(['logging', 'level']))
    print(conf_parser_obj.configParser(['logging', 'level']))
    print(conf_parser_obj.configParser(['logging', 'level']))


"""
读取ini配置文件信息
"""
