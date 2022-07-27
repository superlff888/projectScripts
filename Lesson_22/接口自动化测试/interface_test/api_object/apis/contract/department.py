# -*- coding=utf-8 -*-
# @Time    : 2022/07/27 20:47
# @Author  : ╰☆H.俠ゞ
# =============================================================
import requests

from Lesson_22.接口自动化测试.interface_test.api_object.apis.commonWework.wework_api import Wework


class Department(Wework):

    def create_department(self, _id):
        req = {
                "method": "POST",
                "url": 'https://qyapi.weixin.qq.com/cgi-bin/department/create',
                "params": {  # 注意：params要符合底层框架request用到的params参数，参数名要一致
                    "access_token": self.token
                    },
                "json": {  # 注意：json要符合底层框架request用到的json参数，参数名要一致
                        "name": f"广州研发中心_update_{_id}",
                        "name_en": f"RDGZ_update_{_id}",
                        "parentid": 1,
                        "order": 1,
                        "id": _id
                                }
                }
        # 发起请求
        res = self.send_api(req)  # 实例化时自动调用send_api()方法,Wework继承了BaseApi的send_api()方法，Department继承了Wework的send_api()
        return res

    def update_department(self, _id):

        # 调用更新接口
        req = {
            "method": "POST",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/department/update',
            "params": {
                "access_token": self.token
                },
            "json": {
                "name": f"广州研发中心_update_{_id}",
                "name_en": f"RDGZ_update_{_id}",
                "parentid": 1,
                "order": 2,
                "id": _id
                }
            }
        # 发起请求
        res = self.send_api(req)  # 实例化时自动调用send_api()方法,Wework继承了BaseApi的send_api()方法，Department继承了Wework的send_api()
        return res

    def query_department(self, _id):

        req = {
            "method": "GET",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/department/list',
            "params": {
                "access_token": self.token,
                # "id": _id  #  不传id，查看所有部门
                }
            }
        # 发起请求
        res = self.send_api(req)  # 实例化时自动调用send_api()方法,Wework继承了BaseApi的send_api()方法，Department继承了Wework的send_api()
        return res

    def del_department(self, _id):
        # 定义url
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/delete'
        # 无论哪种请求方法，请求参数在url中，params传参

        req = {
            "method": "GET",
            "url": 'https://qyapi.weixin.qq.com/cgi-bin/department/delete',
            "params": {
                "access_token": self.token,
                "id": _id
                }
            }
        # 发起请求
        res = self.send_api(req)  # 实例化时自动调用send_api()方法,Wework继承了BaseApi的send_api()方法，Department继承了Wework的send_api()
        return res