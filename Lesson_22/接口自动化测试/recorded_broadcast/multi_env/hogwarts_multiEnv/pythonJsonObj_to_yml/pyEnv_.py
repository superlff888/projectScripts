# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 11:36
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
需要用户维护的环境参数
"""

env = {
    "default": "old",  # 通过env["default"]取值 【"dev": "127.0.0.1"】
    "overload": "new",
    "testing-studio":
        {
            "old": "httpbin",  # 默认环境对应的host
            "new": "127.0.0.2"
        }
}

# print(type(env["default"]))  # 字典中的key和values属于str类型

