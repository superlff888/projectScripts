# -*- coding=utf-8 -*-
# @Time    : 2022/07/04 20:41
# @Author  : ╰☆H.俠ゞ
# ===========================================================
import requests

from Lesson_22.接口自动化测试.interface_test.api_object.apis.contract.department import Department

"""
data : 表单传参 payload
json: post请求体json传参
params: url传参
"""


class TestDepartment:

    def setup(self):
        # 定义department_id
        self.department_id = 589
        self.depart = Department()  # 实例化时，自动调用父类init方法

    def test_create_department(self):
        print(self.depart.create_department(self.department_id).json())
        assert self.depart.create_department(self.department_id).json()["errcode"] == 0

    def test_update_department(self):
        assert self.depart.update_department(self.department_id)["errcode"] == 0

    def test_del_department(self):
        assert self.depart.del_department(self.department_id)["errcode"] == 0