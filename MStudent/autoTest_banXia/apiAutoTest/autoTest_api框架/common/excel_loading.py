# -*- coding=utf-8 -*-
# @Time    : 2023/02/02 10:27
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os

import pandas

from autoTest_banXia.apiAutoTest.autoTest_api框架.setting import DIR_NAME, getter


def read_data(filepath, sheet_name):
    """
    :: DIR_NAME项目所在路径，常量
    :: filepath:  相对路径
    ::keep_default_na:  读取文件会出现单元格 N/A,获取不到有效值；设置False获取空字符串
    ::engine:  指定引擎

    希望获取的数据格式  "[[],[],[],[],[],[]]"
    """

    # getter.DIR_NAME 也替换为 DIR_NAME
    pandrxl = pandas.read_excel(getter.DIR_NAME + filepath, sheet_name=sheet_name, keep_default_na=False, engine='openpyxl')
    print(pandrxl)
    # 获取单元格数据
    print(pandrxl.iloc[1, 2])
    # 获取总行和总列
    print(pandrxl.shape)
    lines = pandrxl.shape[0]  # 总行数
    cols = pandrxl.shape[1]  # 总行数
    # 数据解析不包含表头，所以数据是从第二行计算的
    data = []
    case_name = []
    for l in range(lines):  # 行
        line_list = []
        for c in range(cols):  # 列
            if c > 0:  #
                line_list.append(pandrxl.iloc[l, c])
            if c == 0:  # 获取第一列的用例名称
                case_name.append(pandrxl.iloc[l, c])

        data.append(line_list)

    return data, case_name


if __name__ == '__main__':
    relative_path = './data/mtxshop_data.xlsx'
    print(read_data(relative_path, "立即购买")[1])
