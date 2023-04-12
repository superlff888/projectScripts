# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 半夏 
# @Time: 2022-11-27 10:28
# @Copyright：北京码同学
from api.seller.base_seller import BaseSellerApi


class Under(BaseSellerApi):
    def __init__(self, good_id):
        """
        商品下架
        """
        super().__init__()
        self.url = f'{self.host}/seller/goods/{good_id}/under'
        self.method = 'put'
        self.desc = '商品审核'


class Recycle(BaseSellerApi):
    def __init__(self, good_id):
        """
        商品放入回收站
        """
        super().__init__()
        self.url = f'{self.host}/seller/goods/{good_id}/recycle'
        self.method = 'put'
        self.desc = '商品审核'


class DeleteGoods(BaseSellerApi):
    """
    商品彻底删除
    """

    def __init__(self, good_id):
        super().__init__()
        self.url = f'{self.host}/seller/goods/{good_id}'
        self.method = 'delete'
        self.desc = '商品审核'
