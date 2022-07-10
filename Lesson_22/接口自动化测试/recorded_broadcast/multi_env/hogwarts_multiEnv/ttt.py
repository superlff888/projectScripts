# -*- coding=utf-8 -*-
# @Time    : 2022/07/10 15:36
# @Author  : ╰☆H.俠ゞ
# =============================================================
import yaml

data = {
    "method": "get",
    "url": "http://httpsbin.testing-studio.com/get"
}
env_yml = yaml.safe_load(open("env.yml"))  # 读取yaml流文件数据

print(env_yml)
print(env_yml["testing-studio"][env_yml["default"]])
print(env_yml["testing-studio"][env_yml["override"]])
string = data["url"]
print(string)
string = string.replace(env_yml["testing-studio"][env_yml["default"]],
                        env_yml["testing-studio"][env_yml["override"]])  # 先由dict强转json字符串，然后字符串替换,最后重新赋值于字典key
print(f'替换后：{string}')

# s = "123"
# s = s.replace("1", "a")
# print(s)
