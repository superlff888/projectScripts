# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 15:16
# @Author  : ╰☆H.俠ゞ
# =============================================================

from jsonschema import validate, ValidationError, SchemaError


"""
封装schema方法，避免程序走不到assert
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
