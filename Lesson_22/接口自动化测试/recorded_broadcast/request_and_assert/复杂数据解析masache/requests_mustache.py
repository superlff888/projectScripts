# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 13:35
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

import pystache  # 用两个花括号识别变量，可以对变量自动识别和替换

create_emp = {
    "userid": "zhangsan",
    "name": "张三",
    "alias": "jackzhang",
    "mobile": "+86 13800000000",
    "department": [1, 2],
    "order": [10, 40],
    "position": "产品经理",
    "gender": "1",
    "email": "zhangsan@gzdev.com",
    "biz_mail": "zhangsan@qyycs2.wecom.work",
    "is_leader_in_dept": [1, 0],
    "direct_leader": ["lisi", "wangwu"],
    "enable": 1,
    "avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
    "telephone": "020-123456",
    "address": "广州市海珠区新港中路",
    "main_department": 1,
    "extattr": {
        "attrs": [
            {
                "type": 0,
                "name": "文本名称",
                "text": {
                    "value": "文本"
                }
            },
            {
                "type": 1,
                "name": "网页名称",
                "web": {
                    "url": "http://www.test.com",
                    "title": "标题"
                }
            }
        ]
    },
    "to_invite": True,
    "external_position": "高级产品经理",
    "external_profile": {
        "external_corp_name": "企业简称",
        "wechat_channels": {
            "nickname": "视频号名称"
        },
        "external_attr": [
            {
                "type": 0,
                "name": "文本名称",
                "text": {
                    "value": "文本"
                }
            },
            {
                "type": 1,
                "name": "{{name}}",
                "web": {
                    "url": "http://www.test.com",
                    "title": "标题"
                }
            },
            {
                "type": 2,
                "name": "测试app",
                "miniprogram": {
                    "appid": "wx8bd8012614784fake",
                    "pagepath": "/index",
                    "title": "{{title}}"
                }
            }
        ]
    }
}


emp = str(create_emp)


"""
mastache可以极大的简化代码，只需要替换{{}}里面的数据即可
"""


class TestDemo:
    def test_demo(self):
        j = pystache.render("{{say}},{{person}}!", **{"say": "Hi", "person": "lee"})  # 返回给定模板字符串，即template参数
        print(j)

    def test_emp(self):
        # template参数是string类型,所以应先将json转化为字符串
        j = pystache.render(emp, **{"name": "lee", "title": "study hard"})  # 返回给定模板字符串，即template参数
        pprint(j)
