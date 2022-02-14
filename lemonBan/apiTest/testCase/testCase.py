# @Time  : 2021/06/15 16:13
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================
from lemonBan.apiTest.scripts.httpReuquests import HttpRequest

data_url = ('post', 'http://zwmsqas.cttq.com/web/userLoginDetail/login', {"userName": '007', "password": '123456'})
# url, data = ('http://zwmsqas.cttq.com/web/userLoginDetail/login', {"userName": '007', "password": '123456'})


hr = HttpRequest()
response = hr.request(*data_url)
result_json = response.json()
print(result_json)


