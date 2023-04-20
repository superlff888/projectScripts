# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 16:06
# @Author  : ╰☆H.俠ゞ
# =============================================================
f = open('../test.txt', 'r')
content = f.read(5)
print(content)
print("-"*30)
content = f.read()
print(content)
f.close()