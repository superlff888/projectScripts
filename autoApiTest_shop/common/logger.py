

import logging.handlers

# 单例模式的思想：通过逻辑控制，只生成一个对象
from setting import DIR_NAME


class GetLogger:
    """
    当已经创建了logger对象的时候，那么之后就不在创建了，也就是只创建一次对象
    """
    # 把logger对象的初始值设置为None
    logger = None

    # 创建logger，并且返回这个logger
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 创建日志器，控制他的创建次数
            cls.logger = logging.getLogger('autotest')  # 这里的值是自定义的
            # 设置总的级别，debug/info/warning/error
            cls.logger.setLevel(logging.DEBUG)  # 设置debug级别，意味着高于debug的都会被收集
            # 2获取格式器
            # 2.1 要给格式器设置要输出的样式
            fmt = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s():%(lineno)d] - %(message)s"
            # 2.2创建格式器，并且给他设置样式
            fm = logging.Formatter(fmt)
            # 3.创建处理器 按照时间进行切割文件
            tf = logging.handlers.TimedRotatingFileHandler(filename=DIR_NAME + '/logs/requests.log',  # 原日志文件
                                                           when='H',  # 间隔多长时间把日志存放到新的文件中
                                                           interval=1,
                                                           backupCount=3,  # 除了原日志文件，还有3个备份
                                                           encoding='utf-8'
                                                           )
            logging.basicConfig(level=logging.DEBUG, format=fmt)  # 这是在控制台上打印日志信息

            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理器
            cls.logger.addHandler(tf)
        return cls.logger


logger = GetLogger.get_logger()


# if __name__ == '__main__':
#     # aa=AA()
#     # aa.pp()
#     logger = GetLogger().get_logger()
#     # print(id(logger))
#     # logger1 = GetLogger().get_logger()
#     # print(id(logger1))
#     logger.debug('调试')  # 相当print小括号中的信息
#     logger.info('信息')
#     logger.warning('警告')
#     name = 'yaoyao'
#     logger.error('这个变量是{}'.format(name))
#     logger.critical('致命的')
