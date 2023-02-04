# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 13:54
# @Author  : ╰☆H.俠ゞ
# =============================================================
import json

# env = {
#     "default": "dev",  # 通过env["default"]取值 【"dev": "127.0.0.1"】
#     "testing-studio":
#         {
#             "dev": "httpbin",
#             "test": "127.0.0.2"
#         }
# }
env = {'default': 'dev', 'testing-studio': {'dev': 'httpbin', 'test': '127.0.0.2'}}
print(f"env的type为：{type(env)}")
# json.dumps是对python对象编码成json对象，可以把字典转成json字符串
str_env = json.dumps(env, ensure_ascii=False)  # ensure_ascii=False显示中文
print(f"str_env的type为：{type(str_env)}")
print(f"str_env的type为：{str_env}")

# json.loads是将json字符串解码成python对象,可以把json字符串转化为python字典
env_dict = json.loads(str_env)
print(env_dict)
print(f"env_dict的type为：{type(env_dict)}")


def read_out_json_forLoads():
    with open("./data.json") as f:  # f为流文件， f.read() 为字符串
        print(f"{type(f)}")  # <class '_io.TextIOWrapper'>
        # 通过read()读出流文件中str，然后执行loads()加载
        datas = json.loads(f.read())  # loads()方法接收的是一个实例 【a `str``, ``bytes`` or ``bytearray`` instance】
        print(f"datas:{datas}")
        print(f"datas:{type(datas)}")
        print(f"f.read():{type(f.read())}")


def read_out_json_forLoad():
    with open("./data.json") as f:
        print(f"{type(f)}")  # <class '_io.TextIOWrapper'>
        data = json.load(f)  # load()方法接收的fp流文件
        print(f"data:{data}")
        print(f"data:{type(data)}")
        print(type(data))


def write_in_json_forStr():
    with open("data_env.json", "w") as f:  # 以写的模式打开一个文件data_str.json
        f.write(str(env))


def write_in_json_forDump():
    with open("data_env.json", "w") as f:  # 以写的模式打开一个文件data_str.json,即f为文件流
        json.dump(env, f, ensure_ascii=False)  # 将python对象env写入文件中;ensure_ascii=False显示中文


if __name__ == "__main__":
    read_out_json_forLoad()
    # write_in_json_forDump()
    # write_in_json_forStr()