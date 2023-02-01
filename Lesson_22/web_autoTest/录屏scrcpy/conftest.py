# -*- coding=utf-8 -*-
# @Time    : 2023/01/31 21:50
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
1、安卓录屏工具 scrcpy
   - 使用教程 https://blog.csdn.net/was172/article/details/99705855
   - appium（adb）自带录屏功能，但是有可能对某些机型不支持，比如华为会有一些录屏限制
2、适用于web和app
"""
import os
import signal
import subprocess
import sys

import allure
import pytest
from selenium import webdriver


@pytest.fixture(scope="module", autouse=True)  # 模块级别只调用一次；自动调用
def record_video():
    """
    'the function used for record video'.

    :shell : 为True时运行命令
    :stdout : 标准信息输出
    :stderr : 错误信息输出

    sys.path.append(os.path.dirname(__file__))  # 动态添加环境变量
    """
    # 录屏命令
    command = "scrcpy --record tmp.mp4"  # 需配置环境变量

    # 执行命令"scrcpy --record tmp.mp4"，自动开启录屏；需将scrcpy.exe所在目录添加到环境变量
    # sys.path.append("scrcpy.exe绝对路径")  # 动态添加环境变量
    p = subprocess.Popen(args=command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print(p)
    yield '成功录屏'
    os.kill(p.pid, signal.CTRL_C_EVENT)  # 命令行 Ctrl + C 结束录屏进程
