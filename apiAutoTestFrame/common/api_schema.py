# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 22:03
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json

from genson import SchemaBuilder
from jsonschema import validate

from common.my_logger import logger
from setting import DIR_NAME


def buildSchema(obj):
    """构建schema"""
    builder = SchemaBuilder()
    builder.add_object(obj)
    json.dump(builder.to_schema(), open(DIR_NAME+'/data/schema_data.json', 'w', encoding='utf-8'))


def schema_validate(instance, schema):
    """schema数据校验"""
    try:
        validate(instance, schema)
    except Exception as e:
        logger.info(f"异常错误：{e}")
        return False
    else:
        return True