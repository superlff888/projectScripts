# @Time  : 2022/02/10 17:30
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import configparser
import os

"""
封装的原则：
    写死的固定数据（变量），可以封装成类属性，如 配置文件名 config.ini，来控制其他配置文件
    实现某个功能的代码封装成方法，
    在各个方法中都要用到的数据，抽离出来作为实实例属性
封装前，读配置文件数据三部曲：
    conf = configparser.Configparser()  # 实例化
    conf.read('config.ini', encoding='utf8')  # 打开配置文件，然后才可以调用get等方法获取想要的数据
    conf.get(sections, options)  # 获取options数据
"""
##
"""
    conf = configparser.Configparser()  # 实例化
    conf.read('config.ini', encoding='utf8')  # 打开配置文件，然后才可以调用get等方法获取想要的数据
    conf.get(sections, options)  # 获取options数据
"""


class ReadConfig(configparser.ConfigParser):
    config_dic = {}
    config_opt_dic = {}

    def __init__(self, filepath, encoding='utf8'):
        """
        读取配置文件的内容到配置文件解析器对象.


        """
        # 执行完此步骤，就可调用父类的成员属性，相当于把父类的__init__方法和成员属性继承过来了；
        # 之后用子类实例化一个对象后, 这个对象可以'点'出父类对象的成员属性/方法, 当然也可以'点'出自己类对象的成员属性/方法
        super().__init__()  # （括号中不需要传值self）需要配置父类成员属性，做初始化设置，所以要继承__init__方法
        # 通过子类实例对象（self，即conf）调用父类的read方法（继承），加载配置文件(可进一步做参数化)
        self.con_par = self.read(filepath, encoding)

    def configParser(self, sector, item):
        # global value
        value = None
        try:
            value = self.config_dic[sector][item]
        except Exception as e:  # KeyError: 'logging'  字典中没有该key
            print(Exception(f"KeyError: 字典中没有该键:{e},可添加到该字典中"))
            value = self.get(sector, item)
            self.config_opt_dic[item] = value
            self.config_dic[sector] = self.config_opt_dic
        finally:
            return value


if __name__ == '__main__':
    conf_parser_obj = ReadConfig(os.path.abspath("../conf/setting.ini"))
    print(conf_parser_obj.configParser('logging', 'level'))
    print(conf_parser_obj.config_dic)
    print(conf_parser_obj.config_dic["logging"])
    print(conf_parser_obj.configParser('logging', 'level'))

"""
读取ini配置文件信息
"""


