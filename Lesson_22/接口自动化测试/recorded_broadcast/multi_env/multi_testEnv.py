# -*- coding=utf-8 -*-
# @Time    : 2022/03/28 09:13
# @Author  : ╰☆H.俠ゞ
# =============================================================
from unittest import TestCase
from Lesson_22.接口自动化测试.recorded_broadcast.multi_env.env_api import Api


class Test_api(TestCase):
    data = {
        "method": "get",
        "url": "http://httpsbin.testing-studio.com/get"
    }

    def test_send(self):
        api = Api()
        print(api.send(self.data).text)
