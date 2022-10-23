# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""
from typing import Iterator

list_ = [1, 2, 3, 4, 5, 6, 7, 8]
# list_ = "123e4r5t67890o0"
# for i in list_:
#     print(i)

# next(list_)
it = iter(list_)  # 返回迭代器的下一个项目;要和生成迭代器的 iter() 一起使用;迭代器与可迭代对象不是一个概念
print(next(it))  # next()方法接收的是一个迭代器iterator，而不是可迭代对象iterable
print(next(it))

print(isinstance('abc', (Iterator, )))  # 判断'abc'是不是迭代器iterator
