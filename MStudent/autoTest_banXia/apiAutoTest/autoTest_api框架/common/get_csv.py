# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""
import csv
import os
from pprint import pprint

from autoTest_banXia.apiAutoTest.autoTest_api框架.get_filepath import get_project_dirname, get_project_abspath

"""
凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

"""

# print(path)  # join类似字符串拼接，union
path = get_project_abspath(os.path.join(get_project_dirname(), "../data", 'mtxshop_data.csv'))  # get_project_path()为当前文件所在‘目录’，并不是csvTest所在的路径
print(path)

# with open(path) as f:
#     csv_file = csv.reader(f)  # list[]
#     # 返回迭代器的下一个项目;要和生成迭代器的 iter() 一起使用;迭代器与可迭代对象不同
#     headers = next(csv_file)
#     # print(headers)
#     for line in csv_file:
#         print(line)

def getCSV(path, isNext=True):
    list_ = []
    with open(path, encoding='utf-8') as f:
        # The returned object is an iterator.  Each iteration returns a row of the CSV file
        csv_file = csv.reader(f)  # 返回迭代器iterator
        print(csv_file)
        if isNext:  # True表示csv有表头字段
            # 跳过第一行的用法，往往csv文件的第一行为标题名
            next(csv_file)  # 接收迭代器参数，若不是迭代器,需要用iter()方法转化成迭代器；iter(iterable) -> iterator
            for line in csv_file:  # [['Baked', 'Beans'], ['Lovely', 'Spam'], ['Wonderful', 'Spam']]
                list_.append(line)
    return list_


def getCSVDict():
    list_ = []
    with open(path, encoding='utf-8') as f:
        # 若csv有表头，则默认将csv表头字段定义为key;若没有表头，则可以自定义表头key
        csv_file = csv.DictReader(f)  # 视图对象【'csv.DictReader'】格式类似于 list[{},{}] ; 字典中的key为CSV第一行表头字段
        # 迭代器 [{'first_name': 'Baked', 'last_name': 'Beans'}, {'first_name': 'Lovely', 'last_name': 'Spam'}, {'first_name': 'Wonderful', 'last_name': 'Spam'}]
        print(csv_file)  # 视图对象
        for dic in csv_file:  # 按行读取，dict为： {'first_name': 'Baked', 'last_name': 'Beans'}
            list_.append(dic)  # 将读取的每一行放在列表中
    return list_


pprint(getCSVDict())
pprint(getCSV(path, isNext=True))


"""
写入csv文件
"""


# 定义dialect
class my_dialect(csv.Dialect):
    lineterminator = '\n'
    delimiter = '|'
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL


def write_in_csv(filepath, mode='w'):
    # 新建一个文件并按行写入
    with open(filepath, mode) as f:
        writer = csv.writer(f, dialect=my_dialect)
        writer.writerow(('one', 'two', 'three'))
        writer.writerow((1, 2, 3))
        writer.writerow((4, 5, 6))



