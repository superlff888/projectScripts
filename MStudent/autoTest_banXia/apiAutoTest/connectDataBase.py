# -*- coding=utf-8 -*-
# @Time    : 2023/01/29 15:13
# @Author  : ╰☆H.俠ゞ
# =============================================================
import re

import pymysql

"""
未做封装
"""
#
# host = '82.156.74.26'  # 数据慧说话172.17.6.205  82.156.74.26
# port = 3306
# user = 'root'
# password = 'Testfan#123'  # FKaJMxKIjMw%cERy21  Testfan#123
# charset = 'utf8mb4'
# cursorclass = pymysql.cursors.DictCursor

# conn = pymysql.Connection(host=host, port=port, user=user, password=password,
#                           charset=charset, cursorclass=cursorclass)  # 返回字典格式
# # 创建游标，用来储存数据
# cursor = conn.cursor()
# print(type(cursor))
# cursor.execute('select trade_sn from mtxshop_trade.es_order where order_id = 1')
# data = cursor.fetchall()  # 获取查询的所有结果
# print(data)
# #  提取trade_sn
# print(f'查询结果为：{data[0]["trade_sn"]}')
#
# # 关闭游标
# cursor.close()
#
# # 关闭数据库连接
# conn.close()

SQL = 'select trade_sn from mtxshop_trade.es_order where order_id = 1'


class DBConnection:
    def __init__(self, host, user, password, port=3306):
        self.conn = pymysql.Connection(host=host, port=port, user=user, password=password,
                                       charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
        print(self.conn)
        self.cursor = self.conn.cursor()

    # 查询方法
    def select(self, sql):
        print(self.cursor.execute(sql))
        print(self.cursor.fetchall())
        self.cursor.close()

    # 关闭连接对象
    def close_DB(self):
        if self.conn:  # 也可表达为self.conn is not None; None为python类型
            self.conn.close()
            print("连接对象已经关闭")


# if __name__ == '__main__':
#     DB = DBConnection(host, user, password)
#     DB.select(SQL)
#     DB.close_DB()


op = re.compile()
op.match().group()