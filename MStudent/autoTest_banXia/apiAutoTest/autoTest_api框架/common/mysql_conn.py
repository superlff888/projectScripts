# @Time  : 2021/06/16 11:43
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

import pymysql

# 数据慧说话
dbInfo_data_talk = {
    "host": "172.17.6.205",
    "user": "root",
    "password": "FKaJMxKIjMw%cERy21",
    "port": 3306
}
# 配置数据库相关信息
dbInfo = {
    "host": "82.156.74.26",
    "user": "root",
    "password": "Testfan#123",
    "port": 3306
}


# 最关键的是，判断入参形式是可变长，还是收集参数
class DbConnect(object):
    """
    Connect to database of mysql for query target data,then return a `dict`.

    :: charset 编码格式, "utf8mb4"中文编码，并且支持输入法表情
    :: cursorclass 指定返回数据格式,例如 "pymysql.cursors.DictCursor 指定类型为字典"
    :: database mysql中的数据库，例如 "mtxshop_trade"

    """
    def __init__(self, database, db_cof, charset='utf8mb4'):
        # 打开数据库连接
        self.db = pymysql.Connect(database=database,
                                  charset=charset,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)

        # 使用cursor()方法创建游标对象，存储当前数据，后续的游标操作均在该结果中执行
        self.cursor = self.db.cursor()

    def select(self, SQL) -> [dict, list]:
        """ 可用flag进行区分fetchall()、fetchone()、fetchmany(3)"""
        b = self.cursor.execute(SQL)
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


if __name__ == '__main__':
    db = DbConnect("mtxshop_trade", dbInfo, 'utf8')  # 注意：此处为 'utf8',防止因编码报错
    # print(db)
    a = db.select("select member_id,member_name from es_order where trade_sn = '20230206000027'")
    print(f'a: {a}')  # list of dict
    print(f'获取数据行数： {len(a)}')
    print(f"===================格式化后： {'aaa'}{'bbb'}============================")  # 字符串拼接
    db.close()
