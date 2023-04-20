# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-23
desc: 
sample: 
"""
import sys
import requests
sys.path.append(r"/autoTest_banXia/阶段一：python高级编程/接口/util.py")
from util import get_md5

host = r'http://82.156.74.26:9088/'


# def testGet1():
#     url = host + r"/pinter/com/getSku?id=1"
#     response = requests.get(url)
#     print(response.status_code)
#     dict = response.json()
#     print("code", dict["code"])
#     # print(type(response.text))
#     # response.text["code"]
#     print(response.json())
#     print(response.headers)
#     print(type(response.headers))
#     print(response.headers['Content-Type'])
#
#
# def testGet2():
#     url = host + "/pinter/com/getSku"
#     data = {"id": '1'}
#     response = requests.get(url, params=data)
#     print(response.status_code)
#     dict = response.json()
#     print("code", dict["code"])
#     # print(type(response.text))
#     # response.text["code"]
#     print(response.json())
#     print(response.headers)
#     print(type(response.headers))
#     print(response.headers['Content-Type'])
#
#
# def testPost():
#     url = host + "/pinter/com/login"
#     data = {"userName": 'admin', 'password': 1234}
#     response = requests.post(url, data=data)
#     print(f"返回状态码{response.status_code}")
#     # print(type(response.text))
#     # response.text["code"]
#     print(response.json())
#     print(response.headers)
#     print(type(response.headers))
#     print(response.headers['Content-Type'])
#
#
# # json headers
# def testPostJson():
#     url = host + "/pinter/com/register"
#     data = {"userName": "test", "password": "1234", "gender": 1, "phoneNum": "110",
#             "email": "beihe@163.com", "address": "Beijing"}
#     header = {
#         'Content-Type': 'application/json'
#     }
#     response = requests.post(url, json=data, headers=header)
#     print(f"返回状态码{response.status_code}")
#     # print(type(response.text))
#     # response.text["code"]
#     print(response.json())
#     print(response.headers)
#     print(type(response.headers))
#     print(response.headers['Content-Type'])
#
#
# def testPostKvJson():
#     url = host + "/pinter/com/buy"
#     data = {'param': {"skuId": 123, "num": 10}}
#     response = requests.post(url, data=data)
#     print(f"返回状态码{response.status_code}")
#     # print(type(response.text))
#     # response.text["code"]
#     print(response.json())
#     print(response.headers)
#     print(type(response.headers))
#     print(response.headers['Content-Type'])
#
#
# session = requests.session()
#
#
# def testLogin():
#     url = host + "/pinter/bank/api/login"
#     data = {'userName': 'admin', 'password': 1234}
#     response = session.request(url=url, data=data, method='post')
#     print(f"code:{response.status_code},result={response.json()}")
#
#
# def testquery():
#     url = host + "/pinter/bank/api/query?userName=admin"
#     response = session.request(url=url, method="get")
#     print(f"返回状态码{response.status_code}")
#     # print(type(response.text))
#     # response.text["code"]
#     print(response.json())
#     print(response.headers)
#     print(type(response.headers))
#     print(response.headers['Content-Type'])
#
#
# def test_getToken():
#     url = host + "/pinter/bank/api/login2"
#     data = {'userName': 'admin', 'password': 1234}
#     response = requests.post(url=url, data=data)
#     dic = response.json()
#     token = dic.get('data')
#     print(token)
#     print(jsonpath.jsonpath(dic, '$.data'))
#     token = jsonpath.jsonpath(dic, '$.data')[0]
#     return token
#
#
# def testquery2():
#     token = test_getToken()
#     url = host + "/pinter/bank/api/query2?userName=admin"
#     headers = {'testfan-token': token}
#     reponse = requests.get(url, headers=headers)
#     dic = reponse.json()
#     print(dic)
#
#
# def testbaidu():
#     reponse = requests.get("http://www.baidu.com")
#     reponse.encoding = "utf-8"
#     relist = re.findall(r'<title>(.+?)</title>', reponse.text)
#     # <a href=http://v.baidu.com name=tj_trvideo class=mnav>视频</a>
#     relist2 = re.findall(r'<a href=(.+?) name=.+? class=mnav>(.+?)</a>', reponse.text)
#     print(relist)
#     print(relist2)
#
#
# def testpostSign():
#     url = host + "/pinter/com/userInfo"
#     # 手机号码总共11位，前三位需要满足具体运营商，后8位可以随意组合
#     firstThreeNumber = ["134", "135", "136", "137", "138", "139", "147", "150", "152", "157", "158",
#                         "159", "172", "178", "182", "183", "184", "187", "188", "198", "130", "131", "132", "145",
#                         "155",
#                         "156", "166", "171", "175", "176", "185", "186", "166", "133", "149", "153", "173", "177",
#                         "180", "181",
#                         "189", "199"]
#     phone = random.choice(firstThreeNumber) + str(random.randint(10000000, 99999999))
#     # print(phone)
#     # 毫秒
#     timestamp = round(time.time() * 1000)
#     # print(timestamp)
#     toSign = f'{phone}testfan{timestamp}'
#     # print(toSign)
#     sign = get_md5(toSign)
#     json = {"phoneNum": "11111", "optCode": "testfan", "timestamp": "12112121212", "sign": "your sign data"}
#     json['phoneNum'] = phone
#     json['timestamp'] = timestamp
#     json['sign'] = sign
#     print(json)
#     header = {
#         'Content-Type': 'application/json'
#     }
#     response = requests.post(url=url, json=json, headers=header)
#     print(response.json())


def demoUpload():
    # 二进制
    url = host + "/pinter/file/api/upload"
    path = r"/autoTest_banXia/阶段一：python高级编程/接口/验证码1.png"
    file = {"file": open(path, "rb")}
    print(file)
    req = requests.post(url=url, files=file)
    print(req)


if __name__ == '__main__':
    # testGet1()
    # testGet2()
    # testPost()
    # testPostJson()
    # testPostKvJson()
    # testLogin()
    # testquery()
    # test_getToken()
    # testquery2()
    # testbaidu()
    # testpostSign()
    demoUpload()