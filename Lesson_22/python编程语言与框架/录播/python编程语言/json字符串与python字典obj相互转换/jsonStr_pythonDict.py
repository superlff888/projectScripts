# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 13:54
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json


env = {
    "default": "dev",  # 通过env["default"]取值 【"dev": "127.0.0.1"】
    "testing-studio":
        {
            "dev": "httpbin",
            "test": "127.0.0.2"
        }
}

print(f"env的type为：{type(env)}")

# json.dumps是对python对象编码成json对象，可以把字典转成json字符串
str_env = json.dumps(env)
type(str_env)
print(f"str_env的type为：{type(str_env)}")

# json.loads是将json对象解码成python对象,可以把json字符串转化为python字典

env_dict = json.loads(str_env)
print(env_dict)
print(f"env_dict的type为：{type(env_dict)}")
