# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 16:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
Schema会去通过validate方法，验证传入的对象是不是所指定的类型，用于校验响应数据的数据类型
否则抛出一个SchemaError的异常(SchemaUnexpectedTypeError是SchemaError的子类）
"""


import json
from jsonschema import validate
from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.断言assertion.schema.buildSchema import buildSchema
from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.断言assertion.schema.schemaValidate import schema_validate


def test_genson():
    buildSchema({"a": 1, "b": "aaa", "c": "", "d": None})
    _schema = json.load(open("./demo_schema.json"))
    # 不推荐用validate做断言，因为json实例不符合schema标准时程序会抛出异常,从而导致断言为None,即异常后的断言程序就不走了
    assert validate({"a": 1, "b": "aaa", "c": "", "d": None}, _schema)
