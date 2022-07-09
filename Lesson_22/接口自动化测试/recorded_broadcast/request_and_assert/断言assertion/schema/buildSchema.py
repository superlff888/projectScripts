# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 17:09
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json
from pprint import pprint
from genson import SchemaBuilder


def test_buildSchema():
    """
    运用json库中的dump方法，创建json格式的schema文件
    """
    builder = SchemaBuilder()
    builder.add_object({"a": 1, "b": "aaa", "c": "", "d": None})
    builder.add_object({"a": "1", "b": "aaa", "c": ""})
    pprint(type(builder.to_schema()))
    # 将python对象转换成json对象生成一个fp的文件流
    json.dump(builder.to_schema(), open("./demo_schema.json", "w", encoding="utf-8"))