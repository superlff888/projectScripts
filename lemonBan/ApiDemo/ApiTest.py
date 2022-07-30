# @Time  : 2021/06/09 22:57
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================
from requests.sessions import Session

"""
创建一个session会话对象，提供 cookie 持久性、连接池和配置。
"""
session = Session()
sen = session.post(url='https://baidu.com', data=None)
print(f'文本信息{sen.text}')
