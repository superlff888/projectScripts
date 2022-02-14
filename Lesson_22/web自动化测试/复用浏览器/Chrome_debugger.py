# @Time  : 2021/04/19 21:12
# @Author    : House Lee
# -*-coding=utf-8-*-

"""
应用： 绕过登录的操作或要进入比较深深的页面
前提条件：
    1)需要退出当前所有的浏览器（特别注意）->；关闭所有的Chrome，其他(如 Firefox)不影响
    2)找到chrome启动路径->chrome.exe的安装路径（即D:\Program Files\Chrome\Google\Chrome\Application）
    3)配置环境变量->将chrome.exe的安装路径配置到环境变量（path）
    4)启动命令 windows:  chrome --remote-debugging-port=9222  ->(cmd命令执行)
                 mac:  Google\Chrome --remote-debugging-port=9222
    5)访问http://localhost:9222/  ->执行cmd命令的计算机IP（待验证）
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class TestCase:
    def setup_method(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(chrome_options=options)  # options = options 也是ok的；右边options是实例化出的对象

    def teardown_method(self):
        self.driver.quit()

    def test_baidu(self):
        self.driver.get("http://www.baidu.com/")


# if __name__ == '__main__':
#     TestCase()
