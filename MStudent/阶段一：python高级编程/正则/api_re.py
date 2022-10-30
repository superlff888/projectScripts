# -*- coding=utf-8 -*-
# @Time    : 2022/10/30 11:59
# @Author  : ╰☆H.俠ゞ
# =============================================================
import random
import time

import jsonpath
import requests
from utils import get_md5
host = r'http://82.156.74.26:9088/'


def demo_get():
    res = requests.get("/pinter/com/getSku?id=1")
    print(res.json())


def demo_random_tel():
    url = host + "/pinter/com/userInfo"
    header = {
        'Content-Type': 'application/json'
    }
    json = {"phoneNum": "123434", "optCode": "testfan", "timestamp": "1667103266", "sign": "your sign data"}
    first_three_num = ["157", "158", "189", "136", "137", "173", "188"]
    # choice() 从可迭代对象中取一个;sample()是取指定个数
    telephone = random.choice(first_three_num) + str(random.randint(10000000, 99999999))
    print(telephone)
    timestamp = round(time.time()*1000)
    toSign = f'{telephone}testfan{timestamp}'
    sign = get_md5(toSign)
    json["phoneNum"] = telephone
    json["timestamp"] = timestamp
    json["sign"] = sign
    print(json)
    res = requests.post(url=url, json=json, headers=header)
    print(res.json()["data"]['id'])  # json取值
    data = jsonpath.jsonpath(res.json(), '$..data.id')[0]  # jsonpath取值
    print(data)


if __name__ == "__main__":
    demo_random_tel()