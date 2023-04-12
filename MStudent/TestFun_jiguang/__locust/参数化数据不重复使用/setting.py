# -*- coding=utf-8 -*-
# @Time    : 2023/02/02 17:21
# @Author  : ╰☆H.俠ゞ
# =============================================================


import os

"""
获取当前项目所在路径
"""

DIR_NAME = os.path.dirname(__file__)  # __file__  该setting文件固定所在目录，即当前项目所在路径


class GetDirname:
    @property
    def DIR_NAME(self):
        """当前项目所在路径"""
        return os.path.dirname(__file__)


getter = GetDirname()


if __name__ == '__main__':
    print(DIR_NAME)