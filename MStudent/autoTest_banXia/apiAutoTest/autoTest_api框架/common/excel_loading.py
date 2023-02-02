# -*- coding=utf-8 -*-
# @Time    : 2023/02/02 10:27
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
from urllib.parse import urljoin

import xlrd
import pandas

from autoTest_banXia.apiAutoTest.autoTest_api框架.common.get_filepath import get_project_abspath, get_project_dirname


def read_data(filepath, sheet_name):
    """
    ::keep_default_na:  读取文件会出现单元格 N/A,获取不到有效值；设置False获取空字符串
    ::engine:  指定引擎
    """
    panrxl = pandas.read_excel(filepath, sheet_name=sheet_name, keep_default_na=False, engine='openpyxl')
    print(panrxl)


if __name__ == '__main__':
    path = get_project_abspath(os.path.join(get_project_dirname(), "../data/mtxshop_data.xlsx"))
    print(path)
    print(read_data(path, "立即购买"))