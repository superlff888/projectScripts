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
#     headers = next(csv_file)  # 返回迭代器的下一个项目;要和生成迭代器的 iter() 一起使用;迭代器与可迭代对象不是一个对象
#     # print(headers)
#     for line in csv_file:
#         print(line)

with open(path) as f:
    # 若csv有表头，则默认将csv表头字段定义为key;若没有表头，则可以自定义表头key
    csv_file = csv.DictReader(f)  # list[{},{}] ; key为表头字段
    # csv_file = csv.DictReader(f, ['a', 'b'])  # list[{},{}] ; key为表头字段
    print(type(csv_file))

    for line in csv_file:
        print(line)
        # print(line['a'], line['b'])

