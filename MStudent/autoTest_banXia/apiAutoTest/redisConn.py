# -*- coding=utf-8 -*-
# @Time    : 2023/01/30 10:02
# @Author  : ╰☆H.俠ゞ
# =============================================================
import redis

"""
# # redis 取出的结果默认是字节，通过设定 decode_responses=True 改成字符串
# conn_pool = redis.ConnectionPool(host='82.156.74.26', password=None, port=6379, decode_responses=True)
# 
# # 获取redis对象
# r = redis.Redis(connection_pool=conn_pool)
"""


class RedisConn:
    # redis 取出的结果默认是字节，通过设定 decode_responses=True 改成字符串
    def __init__(self, host, password, decode_responses=False, port=6379):  # mtxshop  '82.156.74.26'
        """
        :param host: redis服务器地址
        :param password: redis密码
        :param decode_responses: 默认False，表示返回的是bytes数据

        """
        # 创建连接池
        self.conn_pool = redis.ConnectionPool(host=host, password=password, port=port,
                                              encoding_errors='ignore', decode_responses=decode_responses)
        # 获取redis对象
        self.red = redis.Redis(connection_pool=self.conn_pool)

    def get(self, key):
        Type = self.red.type(key).decode()  # 对二进制数据进行解码
        if Type == 'string':
            return self.red.get(key)
        elif Type == 'hash':
            return self.red.get(key)
        elif Type == 'list':
            return self.red.get(key)
        elif Type == 'set':
            return self.red.get(key)
        elif Type == 'zset':
            return self.red.get(key)
        else:
            raise Exception(f'不支持的数据类型{type}或者{key}不存在！')