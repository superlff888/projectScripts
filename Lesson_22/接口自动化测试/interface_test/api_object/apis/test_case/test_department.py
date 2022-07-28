# -*- coding=utf-8 -*-
# @Time    : 2022/07/04 20:41
# @Author  : ╰☆H.俠ゞ
# ===========================================================
import requests

from Lesson_22.接口自动化测试.interface_test.api_object.apis.contract.department import Department
from Lesson_22.接口自动化测试.interface_test.api_object.apis.utils.loggerMy import logger

"""
data : 表单传参 payload
json: post请求体json传参
params: url传参
"""


class TestDepartment:

    def setup_class(self):
        # 定义department_id
        self.department_id = 2
        self.depart = Department()  # 实例化时，自动调用父类init方法
        try:
            # 尝试删除定义的department_id，排除干扰
            self.depart.del_department(self.department_id)
        except Exception as e:
            logger.info(e)

    def test_create_department(self):
        assert self.depart.create_department(self.department_id).json()["errcode"] == 0

    def test_update_department(self):
        assert self.depart.update_department(self.department_id).json()["errcode"] == 0

    def test_query_department(self):
        assert self.depart.query_department(self.department_id).json()["errcode"] == 0