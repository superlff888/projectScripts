# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 半夏 
# @Time: 2022-11-27 9:57
# @Copyright：北京码同学
from api.buyer.base_buyer import BaseBuyerApi


class GetSkuId(BaseBuyerApi):
    def __init__(self, goods_id):
        super().__init__()
        self.url = f'{self.host}/goods/{goods_id}/skus'
        self.method = 'get'
        self.desc = '商品审核'


if __name__ == '__main__':
    print(GetSkuId(19812).request().text)