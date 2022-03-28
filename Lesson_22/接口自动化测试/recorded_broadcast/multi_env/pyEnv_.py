# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 11:36
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
需要用户维护的环境参数
"""

env = {
    "default": "dev",  # 通过env["default"]取值 【"dev": "127.0.0.1"】
    "testing-studio":
        {
            "dev": "httpbin",
            "test": "127.0.0.2"
        }
}

# print(type(env["default"]))  # 字典中的key和values属于str类型



