# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 21:43
# @Author  : ╰☆H.俠ゞ
# =============================================================
from api.buyer.base_buyer import BaseBuyerApi
from api.buyer.buyer_login import BuyerLoginApi


def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示
    :return :
    """
    for item in items:  # item 为执行的每条用例
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


def token_from_buyerLogin():
    # 买家
    res = BuyerLoginApi().send()
    buyer_token = res.json()["access_token"]
    buyer_uid = res.json()["uid"]
    BaseBuyerApi.BUYER_TOKEN = buyer_token
    BaseBuyerApi.BUYER_UID = buyer_uid
