# -*- coding=utf-8 -*-
# @Time    : 2023/03/03 23:12
# @Author  : ╰☆H.俠ゞ
# =============================================================

import pymysql


class DbConnect(object):
    """
    Connect to database of mysql for query target data,then return a `dict`.

    :: charset 编码格式, "utf8mb4"中文编码，并且支持输入法表情
    :: cursorclass 指定返回数据格式,例如 "pymysql.cursors.DictCursor 指定类型为字典"
    :: database mysql中的数据库，例如 "mtxshop_trade"

    """

    dbInfo = {
        "host": "82.156.74.26",
        "user": "root",
        "password": "Testfan#123",
        "port": 3306
    }

    def __init__(self, database, db_cof, charset='utf8mb4'):
        # 打开数据库连接
        self.db = pymysql.Connect(database=database,
                                  charset=charset,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)

        # 使用cursor()方法创建游标对象，存储当前数据，后续的游标操作均在该结果中执行
        self.cursor = self.db.cursor()

    def select(self, SQL: str) -> [dict, list]:
        """ 可用flag进行区分fetchall()、fetchone()、fetchmany(3)"""
        self.cursor.execute(SQL)
        result = self.cursor.fetchall()  # 获取所有sql结果中数据
        # result = self.cursor.fetchone()  # 从sql结果（self.cursor.execute(sql)）中获取第一条数据
        # result = self.cursor.fetchmany(3)  # 从sql结果（self.cursor.execute(sql)）中获取指定条数数据
        self.db.commit()  # 若不提交事务，下次查询就没有数据
        self.cursor.close()  # 关闭游标; 相当于关闭查询结果,数据库还在连接状态
        return result

    def execute(self, SQL, mode="select") -> dict:
        """
        :param SQL:
        :return:
        """
        if mode == "select":
            try:
                self.cursor.execute(SQL)  # 执行SQL语句
                result = self.cursor.fetchall()
                print(f'执行查询结果为： {result}')
                self.db.commit()  # 提交修改
            except Exception as e:
                # 发生错误时回滚
                self.db.rollback()
                raise e

    def close(self):
        # 关闭数据库的连接
        self.db.close()
