# -*- coding=utf-8 -*-
# @Time    : 2023/01/30 10:02
# @Author  : ╰☆H.俠ゞ
# =============================================================
import redis

# 创建连接池对象； 参数:host、port、数据格式（字符串、列表、哈希、集合、有序集合）
# redis 取出的结果默认是字节，通过设定 decode_responses=True 改成字符串
conn_pool = redis.ConnectionPool(host='82.156.74.26', password=None, port=6379, decode_responses=True)

# 获取redis对象
r = redis.Redis(connection_pool=conn_pool)

r.set("sex", "女")
# r.get('name')
r.hmget()