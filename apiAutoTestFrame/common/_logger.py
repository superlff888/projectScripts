# @Time  : 2021/06/08 22:21
# @Author    : House Lee
# -*-coding=utf-8-*-
import logging

from common.file_load import get_yml
from setting import DIR_NAME

"""
日志配置 https://zhuanlan.zhihu.com/p/454463040
"""


class Logging:

    """
    ::filename 相对路径


    class新创建实例时，会调用__new__，它主要控制一个新实例的创建,即控制类实例创建的规则（__init__方法可以看作运用该规则初始化一个实例），
    __new__必须要有返回值,返回的是当前类的实例; __new__方法正是创建'这个类实例'的方法，
    __new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别

    """

    # 定义了实例被初始化的规则,，你可以把类看成是metaclass元类创建出来的“实例”
    def __new__(cls, filename, level, *args, **kwargs):  # cls 类方法 ；通常用self代表实例方法
        """
        定义一个实例，该实例需要被指定收集器级别，低于该级别的日志将不会被收集
        ：先定义metaclass，就可以创建类，最后创建实例
        :param level: "DEBUG"/"INFO"/"WARNING"/"ERROR"/"CRITICAL"；可单独设置文件日志级别和控制台日志级别
        :param filename: 日志文件所在路径
        :param args:
        :param kwargs:
        """

        level = level.upper()
        # 创建自己的日志收集器
        my_log = logging.getLogger('apiAutoTest')  # 将返回的"my_log"赋值给my_log
        # 设置收集的日志的等级，这里设置为DEBUG（表示只收集DEBUG等级及以上的日志）
        my_log.setLevel(level)  # 日志收集器的级别,级别不够，不会打印到控制台或文件中
        # 创建一个日志输出渠道（输出到控制台）处理器
        l_c = logging.StreamHandler()
        logging.basicConfig()
        # 设置‘输出到控制台的日志’的级别，该级别若低于收集器的级别，则控制台日志将不会被打印
        l_c.setLevel(level)
        # 创建一个日志输出渠道（输出到文件）处理器
        l_f = logging.FileHandler(DIR_NAME + filename, encoding='utf-8')
        # 设置‘输出到文件的日志’的级别 ； 该级别若低于收集器的级别，则日志将不会被打印到文件中
        l_f.setLevel(level)
        # 设置日志输出的格式
        ft = logging.Formatter(
            '%(asctime)s   %(name)s - "%(pathname)s:%(lineno) d" - %(filename)s - %(funcName)s - %(levelname)s  接口请求中……',  # %(message)s
            "%Y-%m-%d %H:%M:%S")
        # 设置渠道（控制台和文件）日志的输出格式
        l_c.setFormatter(ft)
        l_f.setFormatter(ft)
        # 将输出渠道添加到日志收集器中，不管是控制台还是文件，都是要‘收集’的
        my_log.addHandler(l_c)
        my_log.addHandler(l_f)
        return my_log


LEVEL = get_yml('/conf/logs.yml').get("level")
PATH = get_yml('/conf/logs.yml').get("filepath")
logger = Logging(PATH, LEVEL)
