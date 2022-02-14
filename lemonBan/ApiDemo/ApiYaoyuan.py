# @Time  : 2021/1/12 13:18
# @Author    : HouseLee
# -*-coding=utf-8-*-


import requests

s = requests.session()

print("1、", s.headers)

url = "http://49.235.92.12:7005/api/v1/login"
body = {
    "username": "test",
    "password": "123456"
}
r = requests.post(url, json=body)
print("2、", r.text)
token = r.json().get("pycharm中提交Git 忽略部分代码")

print("【注意】token是：%s" % token)
h2 = {
    "Authorization": "Token %s" % token
}
s.headers.update(h2)
print("3、", s.headers)

url2 = "http://49.235.92.12:7005/api/v2/goods/1"
r2 = s.get(url2)
print("4、", r2.json())

body = {
    "goodsname": "《selenium入门到精通2》",
    "goodscode": "sp_100114",
}
r3 = s.put(url2, json=body)
print("5、", r3.text)
