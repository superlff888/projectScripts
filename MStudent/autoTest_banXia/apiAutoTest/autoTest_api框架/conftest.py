# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from autoTest_banXia.apiAutoTest.api基础.redisConn import RedisConn


def pytest_collection_modifyitems(items):
    """
    该方法解决测试用例标题ids中文乱码
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