# -*- coding=utf-8 -*-
# @Time    : 2023/02/06 15:21
# @Author  : ╰☆H.俠ゞ
# =============================================================
import yaml

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.setting import DIR_NAME


def get_yaml(filepath):
    """
    yaml文件读取

    ::filepath  文件相对路径
    """

    with open(DIR_NAME+filepath, mode='r', encoding='utf-8') as f:
        content = yaml.load(f, Loader=yaml.FullLoader)
        return content