# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:33
# @Author  : ╰☆H.俠ゞ
# =============================================================

import pytest
from api.buyer.get_skuid import GetSkuId
from api.buyer.base_buyer import BaseBuyerApi
from api.buyer.buyer_login import BuyerLoginApi
from api.manager.audit_api import AuditApi
from api.manager.base_manager import BaseManagerApi
from api.manager.manager_login import ManagerLoginApi
from api.seller.add_goods import AddGoodsApi
from api.seller.base_seller import BaseSellerApi
from api.seller.delete_goods import Under, Recycle, DeleteGoods
from api.seller.seller_login import SellerLoginApi
from common.file_load import get_yml
from common.mysql_conn import DbConnect
from common.redisConn import RedisConn
from typing import List


# def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
#     # item表示每个测试用例，解决用例名称中文显示问题
#     for item in items:
#         item.name = item.name.encode("utf-8").decode("unicode-escape")
#         item._nodeid = item._nodeid.encode("utf-8").decode("unicode-escape")


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return :
    """
    for item in items:  # item 为执行的每条用例
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 获取redisConn连接对象
@pytest.fixture(scope="function", name="Initialize_a_new_Redis_client")
def got_resConn():
    account = get_yml('/conf/redis.yml').get("mxtshop").get("host")
    psw = get_yml('/conf/redis.yml').get("mxtshop").get("password")
    redis_conn = RedisConn(account, psw)
    return redis_conn


@pytest.fixture()
def db():
    host = get_yml('/conf/db.yml').get("mxtshop").get("host")
    port = get_yml('/conf/db.yml').get("mxtshop").get("port")
    user = get_yml('/conf/db.yml').get("mxtshop").get("user")
    password = get_yml('/conf/db.yml').get("mxtshop").get("password")
    database = get_yml('/conf/db.yml').get("mxtshop").get("database")
    db_cof = {
        "host": host,
        "user": user,
        "password": password,
        "port": port
    }
    # 前置  创建数据库连接对象
    db_conn = DbConnect(database, db_cof)
    # a = db_conn.select("select member_id,member_name from es_order where trade_sn = '20230206000027'")
    # print(db_cof)
    # print(f'a: {a}')  # list of dict
    # print(f'获取数据行数： {len(a)}')
    # print(f"===================格式化后： {'aaa'}{'bbb'}============================")  # 字符串拼接
    yield db_conn
    # 后置  关闭数据库
    db_conn.close()


@pytest.fixture(scope="session", autouse=True)
def get_token():
    """作用对象：测试用例"""
    # 买家
    bla = BuyerLoginApi()
    res = bla.request()
    buyer_token = res.json()["access_token"]
    buyer_uid = res.json()["uid"]
    print(f"买家登录token：{buyer_token}")
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
    BaseManagerApi.manager_token = res.json().get("access_token")  # 需要提取登录token 传递到headers中
    # print(f"manager_token为: {BaseManagerApi.manager_token}")


@pytest.fixture(scope='session')
def create_goods():

    """发布商品 --> 商品审核 --> 获取skuid"""

    # 发布商品
    add_api = AddGoodsApi()
    resp = add_api.request()
    # 提取goods_id
    good_id = resp.json()['goods_id']
    # 商品审核
    audit = AuditApi(goods_id=good_id)
    audit.request()
    # 获取商品的产品id,即 skuid
    get_sku_id = GetSkuId(good_id)
    resp = get_sku_id.request()
    sku_id = resp.json()[0]['sku_id']
    # 将生成的 good_id 和 sku_id 返回 格式是元组
    yield good_id, sku_id
    # 后置:数据清理  下架 --> 放入回收站 --> 彻底删除
    under = Under(good_id)
    under.request()

    recycle = Recycle(good_id)
    recycle.request()

    delete = DeleteGoods(good_id)
    delete.request()
