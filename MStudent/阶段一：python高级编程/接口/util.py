# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-21
desc: 
sample: 
"""
import hashlib
import os


def get_project_path():
    """得到项目路径"""
    return os.path.dirname(__file__)


# md5加密
def get_md5(data):
    md5 = hashlib.md5()
    md5.update(data.encode('utf-8'))
    return md5.hexdigest()


# print(get_project_path())

print(get_md5("admin"))
