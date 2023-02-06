# -*- coding=utf-8 -*-
# @Time    : 2023/02/06 11:28
# @Author  : ╰☆H.俠ゞ
# =============================================================
from api.buyer.base_buyer import BaseBuyerApi
from api.buyer.buy_now import BuyNowApi
from api.buyer.buyer_login import BuyerLoginApi
from common.file_load import conf_parser_obj


class BuyerTradeApi(BaseBuyerApi):
    """
    类实例化一定不能放在init构造方法中，否则会形成递归，造成会导致递归超过最大深度(1000)或内存泄漏等情况

    """

    def __init__(self):  # path, method, params
        # 通过ini配置文件处理本接口的入参
        self.path = conf_parser_obj.configParser(["buyer_trade", "path_buyer_trade"])
        super().__init__()  # 继承后，init构造方法中必须调用父类构造方法; 间接继承父类实例属性需通过该表达式
        self.desc = '创建交易'  # 便于日志信息描述
        self.url = f"{self.host}" + f"{self.path}"
        self.method = conf_parser_obj.configParser(["buyer_trade", "method_buyer_trade"])
        self.data = {'client': 'PC', 'way': 'BUY_NOW'}


if __name__ == '__main__':
    bl = BuyerLoginApi()
    res = bl.request()
    token = res.json()["access_token"]
    uid = res.json()["uid"]
    BaseBuyerApi.buyer_token = token
    BaseBuyerApi.buyer_uid = uid
    buy_now_api = BuyNowApi()  # sku_id=600, num=1
    buy_now_api.request()
    res = BuyerTradeApi().request()
    print(res.json())