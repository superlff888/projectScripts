# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 11:36
# @Author  : ╰☆H.俠ゞ
# =============================================================
"""
需要用户维护的环境参数
"""

env = {
    "default": "old",  # 通过env["default"]取值 【"old": "127.0.0.1"】
    "override": "new",
    "testing-studio":
        {
            "old": "127.0.0.1",  # 默认环境对应的host
            "new": "httpsbin"
        }
}

# print(type(env["default"]))  # 字典中的key和values属于str类型

