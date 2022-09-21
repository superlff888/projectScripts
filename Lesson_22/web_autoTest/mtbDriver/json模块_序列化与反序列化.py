# -*- coding=utf-8 -*-
# @Time    : 2022/09/19 11:54
# @Author  : ╰☆H.俠ゞ
# =============================================================


import json

'''字典的序列化与反序列化'''
dict1 = {'name': 'jiff', 'age': 18, 'other': {'city': 'chongqing', 'doing': 'coding'}}
# 将字典转换为json格式的字符串，序列化 【json入参】
dict2_str = json.dumps(dict1)

print(dict2_str, type(dict2_str))
# 将json格式的字符串转换为字典，反序列化
dict3 = json.loads(dict2_str)
print(dict3, type(dict3))