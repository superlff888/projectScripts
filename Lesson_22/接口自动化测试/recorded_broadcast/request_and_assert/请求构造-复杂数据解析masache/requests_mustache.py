# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 13:35
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
from pprint import pprint

import pystache  # 用两个花括号识别变量，可以对变量自动识别和替换

from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.复杂数据解析masache.utils import read_json


"""
mastache可以极大的简化代码，只需要替换{{}}里面的数据即可
"""


class TestDemo:
    def test_demo(self):
        j = pystache.render("{{say}},{{person}}!", **{"say": "Hi", "person": "lee"})  # 返回给定模板字符串，即template参数
        print(j)

    def test_emp(self):
        # template参数是string类型,所以应先将json转化为字符串
        create_emp = read_json("./create_emp.json")  # json文件跟当前py文件在同一文件夹下
        str_emp = str(create_emp)
        print(str_emp)
        j = pystache.render(str_emp, **{"name": "lee", "title": "study hard"})  # 返回给定模板字符串，即template参数
        pprint(j)
