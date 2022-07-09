# @Time  : 2022/01/26 14:32
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
"""
format格式化
    有点：可以有效利用解包的特性
"""

list_a = [1, 21, 3]
print("年龄{0},姓名{0}or{1},体重{1}{1}{2}".format(*list_a))

dict_a = {"age": 21, "name": "lee", "weigh": 73.25}
print("年龄{age},姓名{name},体重{weigh}".format(**dict_a))
print("年龄:{0},姓名{0}or{1},体重{1} {1} {2}".format(*dict_a))
print(f"\n年龄{list_a[1]},姓名{dict_a['name']}")