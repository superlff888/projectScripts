# @Time  : 2021/06/09 01:11
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================
import logging

"""
创建自己的日志收集器
"""


class MyLogging:
    """
     ctrl+shift+U 大小写转换
    """

    def createLogger(self, level, filename):
        # 创建自己的日志收集器（控制器）
        my_log = logging.getLogger('my_log')  # 将返回的"my_log"赋值给my_log
        # 设置收集的日志的等级，若这里设置为DEBUG（表示只收集DEBUG等级及以上的日志）
        my_log.setLevel(level)
        # 创建一个日志输出渠道（输出到控制台）
        l_c = logging.StreamHandler()
        # 要不要将手机的日志展示出来，就要看这里的配置了
        l_c.setLevel(level)
        # 创建一个日志输出渠道（输出到文件）
        l_f = logging.FileHandler(filename, encoding='utf-8')
        l_f.setLevel(level)
        # 定义日志输出的格式
        ft = logging.Formatter(
            '%(asctime)s - %(name)s - "%(pathname)s: %(lineno)d" - %(funcName)s - %(levelname)s   %(message)s',
            "%Y-%m-%d %H:%M:%S")
        # 设置渠道（控制台和文件）日志的输出格式
        l_c.setFormatter(ft)
        l_f.setFormatter(ft)
        # 将输出渠道添加到日志收集器中
        my_log.addHandler(l_c)
        my_log.addHandler(l_f)
        return my_log  # 此时的收集器已经"技多不压身"

    def __init__(self, _flag: str = None) -> None:
        """
        将收集器赋值给logger._debug,logger._info,logger._warning,logger._error,logger._critical
        :param _flag: 标识符
        """
        if _flag == 'DEBUG':
            # self.createLogger('DEBUG', 'debug.log') 即 实例对象调用createLogger()方法，获得的my_log收集器赋值于_debug，
            # 并将_debug转化为成员变量 self._debug;
            self._debug = self.createLogger('DEBUG', 'debug.log')
        if _flag == 'INFO':
            self._info = self.createLogger('INFO', 'info.log')
        if _flag == 'WARNING':
            self._warning = self.createLogger('WARNING', 'warning.log')
        if _flag == 'ERROR':
            self._error = self.createLogger('ERROR', 'error.log')
        if _flag == 'CRITICAL':
            self._critical = self.createLogger('CRITICAL', 'critical.log')
        # if _flag == 'DEBUG+INFO':
        #     self._debug = self.createLogger('DEBUG', 'debug.log')
        #     self._info = self.createLogger('INFO', 'info.log')
        # if _flag == 'DEBUG+INFO+WARNING':
        #     self._debug = self.createLogger('DEBUG', 'debug.log')
        #     self._info = self.createLogger('INFO', 'info.log')
        #     self._warning = self.createLogger('WARNING', 'warning.log')
        # if _flag == 'DEBUG+INFO+WARNING+CRITICAL':
        #     self._debug = self.createLogger('DEBUG', 'debug.log')
        #     self._info = self.createLogger('INFO', 'info.log')
        #     self._warning = self.createLogger('WARNING', 'warning.log')
        #     self._critical = self.createLogger('CRITICAL', 'critical.log')



