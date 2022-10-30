# @Time  : 2022/01/24 22:42
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import pymysql


def get_conn():
    conn = pymysql.connect(
        host='172.17.6.205',  # 服务器地址
        user='root',  # 用户名
        password='FKaJMxKIjMw%cERy21',  # 密码
        database='dataTalk_dev',  # 数据库名
        charset='utf8mb4'  # 编码格式
    )
    return conn


