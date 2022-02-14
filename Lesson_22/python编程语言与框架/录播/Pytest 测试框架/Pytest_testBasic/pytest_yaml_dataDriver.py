# @Time  : 2022/01/23 13:16
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
import pytest
import yaml


class TestDemo:
    @pytest.mark.parametrize('env', yaml.safe_load(open('env.yml', encoding='utf-8')), ids=['测试环境', '开发环境'])
    def test_demo(self, env):
        if 'test' in env:
            print("这是测试环境")
            print(env)
        elif 'dev' in env:
            print("这是开发环境")
            print(env)
        else:
            print("nothing")
