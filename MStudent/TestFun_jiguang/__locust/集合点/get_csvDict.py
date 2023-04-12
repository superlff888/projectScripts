# -*- coding=utf-8 -*-
# @Time    : 2023/04/11 22:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
import csv

from setting import DIR_NAME


def getCSVDict(path):
    list_ = []
    try:
        with open(DIR_NAME + path, encoding='utf-8') as f:
            # 若csv有表头，则默认将csv表头字段定义为key;若没有表头，则可以自定义表头key
            csv_file = csv.DictReader(f)  # 视图对象【'csv.DictReader'】格式类似于 list[{},{}] ; 字典中的key为CSV第一行表头字段
            # 迭代器 [{'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Lovely', 'last_name': 'Spam'}, {'first_name': 'Wonderful', 'last_name': 'Spam'}]
            for dic in csv_file:  # 按行读取，dict为： {'first_name': 'Baked', 'last_name': 'Beans'}
                list_.append(dic)  # 将读取的每一行放在列表中
        return list_
    except Exception as e:
        raise e

