# -*- coding=utf-8 -*-
# @Time    : 2022/09/27 17:00
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os


def file_read(path):
    with open(path, encoding='utf-8') as f:
        data = f.read()
    return data


def file_copy(path, data):
    with open(path, "w", encoding="utf-8") as f:
        f.write(data)


file_copy("./test[复制].txt", file_read("./test.txt"))

os.rename("./test[复制].txt", "./test[复制1].txt")