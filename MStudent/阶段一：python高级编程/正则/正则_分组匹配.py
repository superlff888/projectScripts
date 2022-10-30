# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-30
desc: 
sample: 
"""

import re


text = "12222@126.com"
if re.match(r'[0-9a-zA-Z_]{1,13}@126.com', text):  # 重复匹配[0-9a-zA-Z_]这样的单字符1到13次；最后返回组合字符
    print('has Email address')
else:
    print('No Email address!')

print(re.findall(r'([0-9a-zA-Z_]{1,13})@(126.com)', text))
