# -*- coding=utf-8 -*-
# @Time    : 2023/02/06 18:14
# @Author  : ╰☆H.俠ゞ
# =============================================================
import yaml

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.setting import DIR_NAME


def write_yml(filepath, data):
    """指定yml文件覆盖写入数据"""
    with open(DIR_NAME+filepath, mode='w', encoding='utf-8') as f:  # mode='w' 覆盖写入
        yaml.dump(data, f, Dumper=yaml.Dumper)

