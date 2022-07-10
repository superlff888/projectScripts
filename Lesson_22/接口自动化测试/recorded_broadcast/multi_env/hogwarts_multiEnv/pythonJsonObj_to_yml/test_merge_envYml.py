# -*- coding=utf-8 -*-
# @Time    : 2022/07/10 14:00
# @Author  : ╰☆H.俠ゞ
# =============================================================
from Lesson_22.接口自动化测试.recorded_broadcast.multi_env.hogwarts_multiEnv.pythonJsonObj_to_yml.configMerge import envMerge,envFind


class Test_merge_yaml:
    """
    ./  同级生成yaml文件
    ../ 所在文件上一层生成yaml文件
    """
    def test_dump(self):
        envMerge("./env.yml")

    def test_save_load(self):
        env_dict = envFind("./env.yml")
        print(env_dict)