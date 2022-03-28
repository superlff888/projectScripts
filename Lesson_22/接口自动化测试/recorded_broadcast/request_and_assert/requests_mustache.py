# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 13:35
# @Author  : ╰☆H.俠ゞ
# =============================================================

import pystache  # 用两个花括号识别变量，可以对变量自动识别和替换

env_temp = {
    "default": "{{default}}",  # 通过env["default"]取值 【"dev": "127.0.0.1"】
    "testing-studio":
        {
            "dev": "http",
            "test": "{{test}}"
        }
}

env = str(env_temp)


class TestDemo:
    def test_demo(self):
        j = pystache.render("{{say}},{{person}}!", **{"say": "Hi", "person": "lee"})  # 返回给定模板字符串，即template参数
        print(j)

    def test_temp(self):
        # template参数是string类型
        j = pystache.render(env, **{"default": "test", "test": "127.0.0.1"})  # 返回给定模板字符串，即template参数
        print(j)