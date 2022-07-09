# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 15:16
# @Author  : ╰☆H.俠ゞ
# =============================================================

from jsonschema import validate, ValidationError, SchemaError


"""
封装schema的validate方法，避免程序在assert断言前抛异常，从而无法在控制台展示具体错误
"""


def schema_validate(obj, schema):
    try:
        validate(instance=obj, schema=schema)
    except ValidationError as err:
        print(err)
        return False
    except SchemaError as err:
        print(err)
        return False
    else:
        return True
