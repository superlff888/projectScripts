# -*- coding=utf-8 -*-
# @Time    : 2022/02/20 20:54
# @Author  : ╰☆H.俠ゞ
# =============================================================

"""
1、退出当前所有浏览器（在任务管理器中关闭谷歌浏览器进程）
2、输入启动命令 chrome --remote-debugging-port=9222，通过命令启动浏览器（打开浏览器，指定端口号9222；此时自动打开一个浏览器）
    -- 只要不关闭该浏览器，就可以一直在该浏览器页面执行自动化测试
3、重启命令行和pycharm

"""

from selenium import webdriver  # 不要导入错了
from selenium.webdriver.chrome.options import Options


def options_demo():
    """
    记录用户操作的cookie等信息，只要不关闭当前debug窗口，就一直可用
    """
    # 定义配置的实例对象
    option = Options()
    # 实例属性修改为 debugger模式启动的ip和端口
    option.debugger_address = "localhost:9222"  # 127.0.0.1:9222
    # 实例化driver的时候，添加option配置
    driver = webdriver.Chrome(options=option)
    driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome")  # debugger模式下打开网页应用


if __name__ == "__main__":
    options_demo()


"""
跳过前面自动化测试步骤，轻松复现出问题的场景，只对问题代码进行调试
"""