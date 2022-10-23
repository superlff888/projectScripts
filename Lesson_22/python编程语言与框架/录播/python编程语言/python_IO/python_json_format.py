# @Time  : 2021/1/12 13:18
# @Author    : House Lee
# -*-coding=utf-8-*-
import json

"""
1、json可以描述多维的数据
2、json由字典和列表组成
3、轻量级的数据交换格式
4、如何使用Json:
    (1)json是标准库；
    (2)常用的几种方法：
        json.dumps(python_obj)  把数据类型转换成字符串
        json.loads(json_string) 把字符串转成json
        json.dump()  把数据类型转换成字符串并储存在文件中

"""

json1_data = {
    "name": ["jerry", "nick"],
    "age": 23,
    "gender": "female"
}
print(f"最初格式展示{json1_data}")
print(f"json1_data数据类型是{type(json1_data)}")
data = json.dumps(json1_data)  # 把python数据类型转化为字符串
print(f"转化格式为data={data}")
print(f"data的数据类型是{type(data)}")
json2_data = json.loads(data)  # 把字符串转换成json
print(f"再次将json格式的【字符串数据类型】--data转化为json【json（字典+列表）】，即jsonjson2_data={json2_data}")
print(f"json2_data的数据类型为{type(json2_data)}")
