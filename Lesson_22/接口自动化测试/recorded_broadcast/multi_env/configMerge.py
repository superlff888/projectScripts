# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 14:07
# @Author  : ╰☆H.俠ゞ
# =============================================================
import yaml

from Lesson_22.接口自动化测试.recorded_broadcast.multi_env.pyEnv_ import env


def envMerge():
    with open("./env.yml", "w") as file:  # 以写的形式创建并打开一个yml文件（因为要写入，故mode = "w"），打开的文件重命名为file
        yaml.safe_dump(env, stream=file)  # 将 Python 对象序列化为 YAML 流存到yml文件中


def envFind():
    with open("./env.yml") as dict_f:  # 以只读的形式打开文件
        env_dict = yaml.safe_load(dict_f)
    return env_dict
    print(env_dict)
    print(f"env_dict的type为：{type(env_dict)}")
