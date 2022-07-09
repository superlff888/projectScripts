# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 16:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
Schema会去通过validate方法，验证传入的对象是不是所指定的类型，用于校验响应数据的数据类型
否则抛出一个SchemaError的异常(SchemaUnexpectedTypeError是SchemaError的子类）
"""


from pprint import pprint
from genson import SchemaBuilder
import json
from jsonschema import validate


def test_buildSchema():
    builder = SchemaBuilder()
    builder.add_object({"a": 1, "b": "aaa", "c": "", "d": None})
    builder.add_object({"a": "1", "b": "aaa", "c": ""})
    pprint(type(builder.to_schema()))
    json.dump(builder.to_schema(), open("./demo_schema.json", "w", encoding="utf-8"))  # 将python对象转换成json对象生成一个fp的文件流


def test_genson():
    _schema = json.load(open("./demo_schema.json"))
    # 不推荐用validate做断言，因为json实例不符合schema标准时会抛出异常，导致程序中断
    assert validate({"a": 1, "b": "aaa", "c": "", "d": None}, _schema)
