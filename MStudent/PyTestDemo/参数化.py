# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-30
desc: 
sample: 
"""
import os

import pytest

from httprequests.parametrizeUtils import getCase, getCase2
from utils import get_project_path


@pytest.mark.parametrize("username",['admin1','张三','admin3'])
def test1(username):
    print("---",username)


@pytest.mark.parametrize("username",{'admin','admin','admin'})
def test1_1(username):
    print("---",username)

@pytest.mark.parametrize("username",['admin','admin','admin'])
def test1_2(username):
    print("---",username)


@pytest.mark.parametrize("username,pwd",[('admin','123456'),('test1','123')])
def test2(username,pwd):
    print(username,pwd)

@pytest.mark.parametrize("username,pwd",[['admin', '123456'], ['test1', '123456']])
def test3(username,pwd):
    print(username,pwd)

test_data = [
    {
        'case': '登入成功',
        'usr': 'admin',  # 正常登入
        'psw': '123456'
    },
    {
        'case': '账号不存在',
        'usr': 'admin1',  # 账号不存在
        'psw': '123456'
    },
    {
        'case': '密码错误',
        'usr': 'admin',  # 密码错误
        'psw': '12345'
    },
    {
        'case': '账号或密码为空',
        'usr': '',  # 账号或密码为空
        'psw': ''
    },
]


@pytest.mark.parametrize('param', getCase())
def test4(param):
    print(param)

@pytest.mark.parametrize("casename,username,pwd",getCase2())
def test5(casename,username,pwd):
    print(casename,username,pwd)
