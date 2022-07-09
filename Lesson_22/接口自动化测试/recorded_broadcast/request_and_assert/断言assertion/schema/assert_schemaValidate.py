# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 17:15
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json

from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.断言assertion.schema.utils import schema_validate


def test_schemaValidate():
    _schema = json.load(open("./demo_schema.json"))
    # 如果直接用jsonschema库中validate，当传入的实例不符合schema标准时会抛出异常，因此就不会执行assert
    assert schema_validate({"a": 1, "b": "aaa", "c": 1, "d": None}, _schema)
