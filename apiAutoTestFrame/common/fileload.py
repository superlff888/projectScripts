# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 22:37
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pandas
import yaml

from setting import DIR_NAME


def get_excel(filename, sheet):

    panpyxl = pandas.read_excel(DIR_NAME+filename, sheet)
    lines = panpyxl.shape[0]
    col = panpyxl.shape[1]

    data = []
    for i in range(lines):
        line_list = []
        for j in range(col):
            line_list.append(panpyxl.iloc[i, j])
        data.append(line_list)
    return data

def get_yml(filename):

    with open(DIR_NAME+filename) as f:
        data = yaml.load(f, yaml.FullLoader)
        return data

