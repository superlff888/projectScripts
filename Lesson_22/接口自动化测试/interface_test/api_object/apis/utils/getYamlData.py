# -*- coding=utf-8 -*-
# @Time    : 2022/07/28 21:15
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os

import yaml


class Utils:

    """获取yaml文件的方法"""

    @classmethod
    def get_yaml_data(cls, filepath):
        # 先获得data文件夹的路径，再与yaml文件拼接
        with open(f'{Utils.get_filepath()}/{filepath}', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    """获取文件路径的方法"""
    @classmethod
    def get_filepath(cls):
        # 获取data文件夹的路径（当前文件路径的上一级是utils，进一步获得utils的下一级data）
        path = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "../data"])  # 路径字符串拼接
        return path

    @classmethod
    def get_log_path(cls):
        # 获取data文件夹的路径（当前文件路径的上一级是utils，进一步获得utils的下一级data）
        path = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "../logs"])  # 路径字符串拼接
        return path

