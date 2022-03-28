# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 09:59
# @Author  : ╰☆H.俠ゞ
# =============================================================
from urllib.parse import quote, unquote

string = '你好啊'
en_str = 'hello'

# 编码
utf8_code = quote(string)  # 默认编码格式是utf-8
print(utf8_code)  # 输出结果：   %E4%BD%A0%E5%A5%BD%E5%95%8A
en_code = quote(en_str)  # 当传入的字符串不是中文时，这个编码会原文输出
print(en_code)

# 设置编码格式
gbk_code = quote(string, encoding='gbk')
print(gbk_code)
# 输出： %E4%BD%A0%E5%A5%BD%E5%95%8A
# 解码
prot_str = unquote(gbk_code, encoding='gbk')
print(prot_str)
# 输出结果： 你好啊
