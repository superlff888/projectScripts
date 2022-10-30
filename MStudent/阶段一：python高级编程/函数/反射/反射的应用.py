# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""
import configparser
import os
from utils import get_project_path


# 方式1
def read_settings():
    setting_dic = {}
    config = configparser.ConfigParser()
    path = os.path.join(get_project_path(), "../../文件处理/files/settings.ini")  # 注意路径
    config.read(path, "utf-8")  # 先打开(Read and parse)文件,才能对文件内容操作；注意区别于普通的打开方式
    print(config.get("settings", "proxy_host"))
    list_ = config.items("settings")  # Return a list of (name, value) tuples for each option in a section
    # print(list_)
    for k, v in list_:
        setting_dic[k] = v

    # print(setting_dic)
    return setting_dic


class Settings:
    def __init__(self):
        self.proxy_host = None
        self.proxy_port = None
        self.proxy_id = None
        self.proxy_secret = None
        self.min_inventory = None
        self.wx_url = None


# 方式2
def read_settings2():
    # setting_dic={}
    settings = Settings()
    config = configparser.ConfigParser()
    path = os.path.join(get_project_path(), "../../文件处理/files/settings.ini")  # get_project_path()方法所在目录
    config.read(path, "utf-8")
    list_ = config.items("settings")
    # print(list_)
    for k, v in list_:
        setattr(settings, k, v)

    # print(settings.__dict__)
    return settings


if __name__ == '__main__':
    read_settings()
    # settings = read_settings2()
    # print(settings.__dict__)
    # print(settings.proxy_id)
