# @Time  : 2022/01/21 11:20
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
# import openpyxl
# import csv
#
# book = openpyxl.load_workbook("C:\\Users\\HouseLee\\Desktop\\openpyxl.xlsx")
#
# sheet = book.active
# # 读取单个单元格
# cell1 = sheet['C3']
# cell2 = sheet.cell(3, 3)
# print(cell1.value)
# print(cell2.value)
#
#
# # 读取 data目录下的 params.csv 文件
#
#
# def get_csv():
#     """
#     获取csv数据
#     :return: 返回数据的结构：[[1, 1, 2], [3, 6, 9], [100, 200, 300]]
#     """
#     with open('C:\\Users\\HouseLee\\Desktop\\demo.csv', 'r') as files:
#         raw = csv.reader(files)
#         data = []
#         for line in raw:
#             data.append(line)
#     return data
#
#
# datas = get_csv()
# print(datas)
#
import pytest

"""
单个参数
"""
# search_list = ['appium', 'selenium', 'pytest']
#
#
# # “name”是定义的参数，用列表search_list的三个元素做参数化;当然也可以用元组的三个元素
# @pytest.mark.parametrize("name", search_list)
# def test_search(name):  # 参数化的时候，参数不要有默认值
#     assert name in search_list


"""
多个参数
"""


@pytest.mark.parametrize('test_input, test_expect', [("1+2", 3), ("2+3", 6), ('5+3', 8)], ids=['result_a', "result_b", "result_c"])
def test_mark_more(test_input, test_expect):
    assert eval(test_input) == test_expect


"""
笛卡尔积:运用两个装饰器
"""


@pytest.mark.parametrize('code', ['utf-8', 'gbk', 'gb2312'])
@pytest.mark.parametrize('wd', ['a', 'b', 'c'])
def test_cartesian(wd, code):
    print(f'wd:{wd};code:{code}')