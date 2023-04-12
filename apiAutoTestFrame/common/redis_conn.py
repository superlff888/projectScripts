# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 22:54
# @Author  : ╰☆H.俠ゞ
# =============================================================
import redis


class RedisConn:

    def __init__(self, host, password, decode_responses=False, port=6379):
        self.conn_pool = redis.ConnectionPool(host=host, password=password, port=port,
                                              encoding='error', encode_responses=decode_responses)

        self.redis = redis.Redis(connection_pool=self.conn_pool)

    def get(self, key):
        """key是redis的键，值的数据类型为string、hash、list、set、zset"""
        Type = self.redis.type(key).decode('utf-8')

        if Type == 'string':
            return self.redis.get(key)
        elif Type == 'list':
            return self.redis.lrange(key, 0, -1)
        elif Type == 'hash':
            return self.redis.hgetall(key)
        elif Type == 'set':
            return self.redis.smembers(key)
        else:
            raise Exception(f"不支持的数据类型{Type}或者{key}不存在")
