# @Time  : 2021/06/16 11:43
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
"""
假如该from . import x 语句存在于proj/test.py中，它会导入同级目录下的__init__.py即proj/__init__.py中的x对象
"""
from . import get_conn  # 从init模块中导入方法，获取连接对象
import pymysql

'''
pip install PyMySQL==0.9.3
'''

# 配置数据库相关信息
dbinfo = {
    "host": "172.17.6.205",
    "user": "root",
    "password": "FKaJMxKIjMw%cERy21",
    "port": 3306
}


# 最关键的是，判断入参形式是可变长，还是收集参数
class DbConnect(object):
    """
    :收集参数 : **db_cof解包后，相当于"host"="172.17.6.205"；可不传，也可以集合方式传入多个
    :可变长参数 ：假如dbinfo=("host","user","password","port"),元组*dbinfo解包后，顺序入参，此处联系不定长入参;
                相反：若a,b,c,d = ("host","user","password","port")，此时形参a = "host";
                可不传，也可传入对个
    """
    def __init__(self, database, db_cof, charset=None):
        # 打开数据库连接
        # 解包后，相当于"host" = "172.17.6.205"；键和值一定要跟所在方法的形参和实参对应起来
        self.db = pymysql.connect(database=database,
                                  charset=charset,
                                  cursorclass=pymysql.cursors.DictCursor,  # 该参数可不写（另：此处参数相当于a=1，故init不需要另设形参去接收）
                                  **db_cof)  # 定义的函数中是解包

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
        print(f'self.cursor为： {self.cursor}')
        print(f'dbinfo为： {db_cof}')

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE
        #        WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        # results = self.cursor.fetchall() # 获取所有sql结果中数据
        # re = self.cursor.fetchone() # 从sql结果（self.cursor.execute(sql)）中获取第一条数据
        re_m = self.cursor.fetchmany(3)  # 从sql结果（self.cursor.execute(sql)）中获取指定条数数据
        return re_m

    def execute(self, sql):
        """
        可用flag进行区分fetchall()、fetchone()、fetchmany(3)
        :param sql:
        :return:
        """
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
            b = self.cursor.execute(sql)  # 执行SQL语句
            print(f'excute执行结果为： {b}')
            self.db.commit()  # 提交修改
        except Exception as e:
            # 发生错误时回滚
            self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


if __name__ == '__main__':
    db = DbConnect("dt_qas", dbinfo, 'utf8mb4')  # 注意：此处为 推荐'utf8mb4',防止因编码报错;也可以utf-8
    print(db)
    sql = "SELECT * FROM dt_cdm_salesdata_dept where dept01_cd = '00001903' and sale_date = '20210516';"
    a = db.select(sql)
    print(f'a: {a}')  # list of dict
    print(f'获取数据行数： {len(a)}')
    print(dbinfo)
    print(f"===================格式化后： {'aaa'}{'bbb'}============================")  # 字符串拼接
    db.execute(sql)
    db.close()
