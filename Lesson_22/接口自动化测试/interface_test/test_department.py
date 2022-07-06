# -*- coding=utf-8 -*-
# @Time    : 2022/07/04 20:41
# @Author  : ╰☆H.俠ゞ
# ===========================================================
import requests

"""
data : 表单传参
json: post请求体json传参
params: url传参
"""


class TestDepartment:

    def setup_class(self):
        # 定义凭证信息
        self.corpid = 'wwba697e4878807a9f'
        self.corpsecret = '631qSHbvs5vyhpFQmp7a5AJXM0jWzP-_yOO8EUX6JNU'
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        param = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }

        # 发起get请求，获取token
        res = requests.get(url=url, params=param)
        print(f"获取token：{res.json()}")
        self.token = res.json()["access_token"]

    def setup(self):
        # 定义department_id
        self.department_id = 588
        try:
            # 尝试删除定义的部门id，排除干扰（我们传入的id可能是不存在的部门id）
            self.del_department(self.department_id)  # 调用接口，删除已存在部门id
        except Exception as e:
            print(e)

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

    def test_update_department(self):
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
        assert res.json()["errcode"] == 0