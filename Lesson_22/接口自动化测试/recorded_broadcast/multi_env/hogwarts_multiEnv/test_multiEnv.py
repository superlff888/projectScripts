# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 09:13
# @Author  : ╰☆H.俠ゞ
# =============================================================

from Lesson_22.接口自动化测试.recorded_broadcast.multi_env.hogwarts_multiEnv.env_api import Api


class Test_api:

    data = {
        "method": "get",
        "url": "http://127.0.0.1.testing-studio.com/get"
    }

    def test_send(self):
        api = Api()
        print(api.send(self.data))
