# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 17:09
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json
from pprint import pprint
import yaml
from genson import SchemaBuilder


def buildSchema(obj):
    """
    通过requests库获得的响应一般为python对象(如 dict、list)； 文件流(输入流write、输出流read)需要open，达到可读写状态。

    1、每次运行的时候自动保存当前的schema，下次运行对比上次的schema如果发现变更就报错（运用json库中的dump方法，创建json格式的schema文件）
    2、可以将接口响应值保存为schema
        :: 例如 响应值为 {"a": 1, "b": "aaa", "c": "", "d": None}
    3、 （1） open("./demo_schema.json", "w", encoding="utf-8")   这样是可写流文佳
        （2） "./demo_schema.json"  这样写是相对路径
    """
    builder = SchemaBuilder()
    builder.add_object(obj)
    pprint(type(builder.to_schema()))

    # dump可将python对象序列化为json，并依据open方法的可写mode自动将json写入流文件
    json.dump(builder.to_schema(), open("./demo_schema.json", "w", encoding="utf-8"))


def buildSchemaMulti(obj, fp="./demo_schema.json"):  #
    """
    预期接口响应转化为schema, 接口预期响应字段值可能是integer,也可能是string
    :: 参数 obj  序列化参数，set or dict
        for example:
            ({"x": 1, "y": {"a": 3, "b": "a"}}, {"x": "1", "y": {"a": 3, "b": 8}})
    """

    build = SchemaBuilder()
    for l in obj:  # 遍历
        build.add_object(l)  # 将可能的响应类型都放进去，如 int 8, string "a"
    # pprint(type(build.to_schema()))
    # pprint(build.to_schema())

    # 先转换为schema，然后将python对象(schema)转换成json文件流(fp = "./demo_schema.json")
    json.dump(build.to_schema(), open(fp, "w", encoding="utf-8"))

    # print("====================================================\n")
    # x, y = obj
    # build = SchemaBuilder()
    # build.add_object(x)
    # build.add_object(y)
    # pprint(build.to_schema())


if __name__ == '__main__':
    obj = {"a": 1, "b": "aaa", "c": "", "d": None}
    print(type(obj))
    buildSchema(obj)
