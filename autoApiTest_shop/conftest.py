# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:33
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from api.buyer.base_buyer import BaseBuyerApi
from api.buyer.buyer_login import BuyerLoginApi
from api.manager.base_manager import BaseManagerApi
from api.manager.manager_login import ManagerLoginApi
from api.seller.base_seller import BaseSellerApi
from api.seller.seller_login import SellerLoginApi
from common.file_load import conf_parser_obj
from common.mysql_conn import DbConnect
from common.redisConn import RedisConn

"""

def pytest_collection_modifyitems1(items):
    ''''''
    该方法解决测试用例标题ids中文乱码
    ''''''
    for item in items:  # item指的是每一条用例
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.split('::')[0] + '::' + item.nodeid.split('::')[1].encode("utf-8").decode(
            "unicode_escape")

"""


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return:
    """
    for item in items:  # item为执行的每条用例
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 获取redisConn连接对象
@pytest.fixture(scope="function", name="Initialize_a_new_Redis_client")
def got_resConn():
    account = conf_parser_obj.configParser(["redis", "account"])
    psw = conf_parser_obj.configParser(["redis", "psw"])
    redis_conn = RedisConn(account, psw)
    return redis_conn


@pytest.fixture(scope="function")
def db():
    host = conf_parser_obj.configParser(["mysql", "host"])
    port = int(conf_parser_obj.configParser(["mysql", "port"]))
    user = conf_parser_obj.configParser(["mysql", "user"])
    password = conf_parser_obj.configParser(["mysql", "password"])
    database = conf_parser_obj.configParser(["mysql", "database"])
    db_cof = {
        "host": host,
        "user": user,
        "password": password,
        "port": port
    }
    # 前置  创建数据库连接对象
    db_conn = DbConnect(database, db_cof)
    yield db_conn
    # 后置  关闭数据库
    db_conn.close()


@pytest.fixture(scope="session")
def get_token():
    """作用对象：测试用例"""
    # 买家
    bla = BuyerLoginApi()
    res = bla.request()
    buyer_token = res.json()["access_token"]
    buyer_uid = res.json()["uid"]
    BaseBuyerApi.buyer_token = buyer_token
    BaseBuyerApi.buyer_uid = buyer_uid

    # 卖家
    sla = SellerLoginApi()
    res = sla.request()
    seller_token = res.json()["access_token"]
    seller_uid = res.json()["uid"]
    BaseSellerApi.seller_token = seller_token
    BaseSellerApi.seller_uid = seller_uid

    # 管理员
    mla = ManagerLoginApi()
    res = mla.request()
    BaseManagerApi.manager_token = res.json().get("access_token")
    # print(f"manager_token为: {BaseManagerApi.manager_token}")


# if __name__ == '__main__':
#     get_token()