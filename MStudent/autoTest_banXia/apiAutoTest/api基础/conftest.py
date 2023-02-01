# -*- coding=utf-8 -*-
# @Time    : 2023/01/28 22:26
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from autoTest_banXia.apiAutoTest.api基础.redisConn import RedisConn


def pytest_collection_modifyitems(items):
    """
    该方法解决
    """
    for item in items:  # item指的是每一条用例
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.split('::')[0] + '::' + item.nodeid.split('::')[1].encode("utf-8").decode(
            "unicode_escape")


# 获取redisConn连接对象
@pytest.fixture()
def got_resConn():
    redis_conn = RedisConn('82.156.74.26', 'mtx')
    return redis_conn