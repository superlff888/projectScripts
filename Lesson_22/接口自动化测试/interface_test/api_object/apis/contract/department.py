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
        return res

    def update_department(self, _id):
        # 定义url
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/update"
        param = {
            "access_token": self.token
        }
        json_update_body = {
            "name": f"广州研发中心_update_{_id}",
            "name_en": f"RDGZ_update_{_id}",
            "parentid": 1,
            "order": 2,
            "id": _id
        }
        # 调用更新接口
        res = requests.post(url=url, params=param, json=json_update_body)
        return res.json()

    def query_department(self, _id):
        # 定义url
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list'
        # 无论哪种请求方法，请求参数在url中，params传参
        param = {
            "access_token": self.token,
            "id": _id
        }
        res = requests.get(url=url, params=param)
        return res.json()

    def del_department(self, _id):
        # 定义url
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        # 无论哪种请求方法，请求参数在url中，params传参
        param = {
            "access_token": self.token,
            "id": _id
        }
        res = requests.get(url=url, params=param)
        return res.json()