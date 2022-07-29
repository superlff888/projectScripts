# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 17:15
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json

import pytest

from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.断言assertion.schema.buildSchema import buildSchema
from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.断言assertion.schema.utils import schema_validate
from Lesson_22.接口自动化测试.recorded_broadcast.request_and_assert.断言assertion.schema.utils import schema_validate_max


@pytest.mark.parametrize('obj', [{"a": "1", "b": "aaa", "c": "", "d": None}], ids=["校验响应数据类型"])  # ids=[]
def test_schemaValidate(obj):
    """
    schema_validate失败断言：
        '1' is not of type 'integer'

        Failed validating 'type' in schema['properties']['a']:
        {'type': 'integer'}

        On instance['a']:

        '1'
    【总结】断言信息清晰，便于提高效率
    """

    buildSchema({"a": 1, "b": "aaa", "c": "", "d": None})  # 上次请求的响应值生成的schema
    _schema = json.load(open("./demo_schema.json"))
    # 如果直接用jsonschema库中validate，当传入的实例不符合schema标准时会抛出异常，因此就不会正常执行assert
    assert schema_validate_max([obj, _schema])
