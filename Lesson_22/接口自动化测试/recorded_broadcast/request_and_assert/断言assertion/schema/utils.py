# -*- coding=utf-8 -*-
# @Time    : 2022/07/09 15:16
# @Author  : ╰☆H.俠ゞ
# =============================================================

from jsonschema import validate, ValidationError, SchemaError

from Lesson_22.接口自动化测试.interface_test.api_object.apis.utils.loggerMy import logger

"""
封装schema的validate方法，避免程序在assert断言前抛异常，从而无法在控制台展示具体错误
"""


def schema_validate_max(arg, schema=None):
    """不仅支持单形参，还支持元组和字典等序列"""
    if schema is None:
        "scheme为None时，传参为 obj实例 和 标准schema组成的元组等序列"
        try:
            validate(*arg)
        except ValidationError as err:
            logger.info(f"异常错误：{err}")
            return False
    else:
        try:
            "scheme不为None时，传参为 obj实例 和 标准schema"
            validate(instance=arg, schema=schema)
        except ValidationError as err:
            logger.info(err)
            return False
        except SchemaError as err:
            logger.info(err)
            return False
        else:
            return True


def schema_validate(obj, schema):
    try:
        validate(instance=obj, schema=schema)
    except ValidationError as err:
        logger.info(err)
        return False
    except SchemaError as err:
        logger.info(err)
        return False
    else:
        return True

