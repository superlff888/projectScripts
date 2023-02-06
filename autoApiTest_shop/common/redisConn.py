# -*- coding=utf-8 -*-
# @Time    : 2023/01/30 10:02
# @Author  : ╰☆H.俠ゞ
# =============================================================
import javaobj
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
    def __init__(self, host, password, decode_responses=False, port=6379):
        """
        :param host: redis服务器地址
        :param password: redis密码
        :param decode_responses: 默认False，表示返回的是bytes数据
                                decode_responses=False，java序列化后数据格式为bytes二进制，所以此处为False.
        """
        # 创建连接池；# 【mtxshop】 host '82.156.74.26'  password  "mtx"
        self.conn_pool = redis.ConnectionPool(host=host, password=password, port=port,
                                              encoding_errors='ignore', decode_responses=decode_responses)
        # 获取redis对象
        self.red = redis.Redis(connection_pool=self.conn_pool)

    def get(self, key):
        """key为redis的键; 值的数据类型为：string、hash、list、set、zset"""
        Type = self.red.type(key).decode('utf-8')  # 对二进制数据进行解码
        if Type == 'string':
            return self.red.get(key)
        elif Type == 'hash':
            return self.red.hgetall(key)
        elif Type == 'list':
            return self.red.lrange(key, 0, -1)
        elif Type == 'set':
            return self.red.smembers(key)
        elif Type == 'zset':
            return self.red.zrange(key, 0, -1)
        else:
            raise Exception(f'不支持的数据类型{type}或者{key}不存在！')


if __name__ == '__main__':
    # 获取连接对象
    redis_conn = RedisConn('82.156.74.26', 'mtx')
    # 商城项目; 数据类型为字符串
    bContent = redis_conn.get('{BUY_NOW_ORIGIN_DATA_PREFIX}_24216')
    print(bContent)
    # 从redis缓存中将Java序列化Value转换为二进制(bytes)python对象
    resList = javaobj.loads(bContent)
    print(resList)
    obj = resList[0]  # java对象
    print(obj)
    print(dir(obj))  # dir()返回参数对象的属性、方法列表
    print(obj.__getattribute__("skuId"))  # 获取'skuId'属性值
    print(obj.__getattribute__("num"))  # 获取'num'属性值
