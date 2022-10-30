# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-26
desc: 
sample: 
"""
import pytest


def pytest_collection_modifyitems(items):
    """
    该方法解决
    """
    for item in items:  # item指的是每一条用例
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.split('::')[0] + '::' + item.nodeid.split('::')[1].encode("utf-8").decode("unicode_escape")
