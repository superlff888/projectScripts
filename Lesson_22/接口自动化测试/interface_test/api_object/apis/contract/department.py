# -*- coding=utf-8 -*-
# @Time    : 2022/07/27 20:47
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests

from Lesson_22.接口自动化测试.interface_test.api_object.apis.common.wework_api import Wework


class Department(Wework):

    def create_department(self, _id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/create'
        param = {
            "access_token": self.token
        }

        json_create_body = {
            "name": f"广州研发中心_update_{_id}",
            "name_en": f"RDGZ_update_{_id}",
            "parentid": 1,
            "order": 1,
            "id": _id
        }
        # 发起请求
        res = requests.post(url=url, params=param, json=json_create_body)
        print(res.json())
        # 断言
        # assert res.json()["errcode"] == 0

    def del_department(self, _id):
        # 定义url
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        # 无论哪种请求方法，请求参数在url中，params传参
        param = {
            "access_token": self.token,
            "id": _id
        }
        res = requests.get(url=url, params=param)
        print(res.json())

    def update_department(self):
        # 创建部门id
        self.create_department(self.department_id)
        # 定义url
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        param = {
            "access_token": self.token
        }
        json_update_body = {
            "name": f"广州研发中心_update_{self.department_id}",
            "name_en": f"RDGZ_update_{self.department_id}",
            "parentid": 1,
            "order": 1,
            "id": self.department_id
        }
        # 调用更新接口
        res = requests.post(url=url, params=param, json=json_update_body)
        assert res.json()["errcode"] == 60020

    def query_department(self, _id):
        # 定义url
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        # 无论哪种请求方法，请求参数在url中，params传参
        param = {
            "access_token": self.token,
            "id": _id
        }
        res = requests.get(url=url, params=param)
        print(res.json())