# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 17:09
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json
from pprint import pprint
from genson import SchemaBuilder


def buildSchema(obj):
    """
    1、每次运行的时候自动保存当前的schema，下次运行对比上次的schema如果发现变更就报错（运用json库中的dump方法，创建json格式的schema文件）
    2、可以将接口响应值保存为schema
        :: 例如 响应值为 {"a": 1, "b": "aaa", "c": "", "d": None} 和
    """
    builder = SchemaBuilder()
    builder.add_object(obj)
    # builder.add_object({"a": "1", "b": "aaa", "c": ""})  #
    # pprint(type(builder.to_schema()))

    # 将python对象转换成json对象生成一个fp的文件流
    json.dump(builder.to_schema(), open("./demo_schema.json", "w", encoding="utf-8"))


def buildResponseSchema(obj, fs):
    """
    1、每次运行的时候自动保存当前的schema，下次运行对比上次的schema如果发现变更就报错（运用json库中的dump方法，创建json格式的schema文件）
    2、可以将接口响应值保存为schema
        :: 参数 obj 实际共工作中应该是接口响应值，旨在将每次接口响应值转化为schema保存在json文件中
    """

    builder = SchemaBuilder()
    builder.add_object(obj)
    pprint(type(builder.to_schema()))
    # 将python对象转换成json对象生成一个fp的文件流
    json.dump(builder.to_schema(), open("./demo_schema.json", "w", encoding="utf-8"))