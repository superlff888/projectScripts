# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""
import csv
import os

from utils import get_project_path


path = os.path.join(get_project_path(), "files", 'userTest.csv')  # get_project_path()为utils所在目录，并不是csvTest所在的路径
print(path)  # join类似字符串拼接，union


# with open(path, mode="w") as f:  # path必须是预先创建的？
#     f.write("222\n")


# with open(path) as f:
#     csv_file = csv.reader(f)  # list[]
#     # 返回迭代器的下一个项目;要和生成迭代器的 iter() 一起使用;迭代器与可迭代对象不是一个对象
#     headers = next(csv_file)
#     # print(headers)
#     for line in csv_file:
#         print(line)

def getCSV(path, isNext=True):
    list_ = []
    with open(path, encoding='utf-8') as f:
        csv_file = csv.reader(f)  # 返回迭代器iterator
        if isNext:  # True表示csv有表头字段
            # 跳过第一行的用法，往往csv文件的第一行为字段名
            next(csv_file)  # 接收迭代器参数，若不是迭代器,需要用iter()方法转化成迭代器；iter(iterable) -> iterator
            for line in csv_file:  # [['Baked', 'Beans'], ['Lovely', 'Spam'], ['Wonderful', 'Spam']]
                list_.append(line)
    return list_


def getCSVDict():
    list_ = []
    with open(path, encoding='utf-8') as f:
        # 若csv有表头，则默认将csv表头字段定义为key;若没有表头，则可以自定义表头key
        csv_file = csv.DictReader(f)  # 视图对象【'csv.DictReader'】格式类似于 list[{},{}] ; 字典中的key为CSV第一行表头字段
        for dic in csv_file:  # 按行读取，dict为： {'first_name': 'Baked', 'last_name': 'Beans'}
            list_.append(dic)  # 将读取的每一行放在列表中
    return list_


print(getCSV())