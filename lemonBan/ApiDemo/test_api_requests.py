# @Time  : 2021/05/20 13:39
# @Author    : House Lee
# -*-coding=utf-8-*-
import json
import pprint
import re

from deepdiff import DeepDiff
import pytest
import requests
import jsonpath


def test_a():

    para = {
        "dtype": "json",
        "key": "895694a2c24baf816de553242eb86d08"
    }
    # x = json.dumps(para)
    # print(type(x))
    url = 'http://apis.juhe.cn/cnoil/oil_city'

    r = requests.post(url=url, data=para)  # data/json是由接口文档决定
    print(f'\n{type(r.text)}')
    # 以文本的形式打印响应结果
    print(f'\n{r.text}')
    # 打印type： dict
    print(f'返回的json: {r.json()}')
    print(type(r.json()))
    r_dict = r.json()
    # 将dict类型结果result转换成json格式
    r_json = json.dumps(r_dict, sort_keys=True, indent=2)
    print(f'r_json的type为：\n{type(r_json)}')

    # print(r.encoding)
    # print(r.status_code)
    # result_str = re.search('("reason"):(.{11}.)', r.text)  # search返回的是匹配的是str
    # print(f'result.group()的type：{type(result_str.group())}')
    # result_str_list = re.findall('("reason"):(.{11}.)', r.text)  # findall返回的是list
    # print(f"r1为{type(result_str_list)}")
    # print(result_str_list[0][1])
    # # assert '"reason":"当前可请求的次数不足"' in result
    # pytest.assume(result_str.group() == '"reason":"当前可请求的次数不足"')
    # pytest.assume(r.status_code == 200)
    # pytest.assume(result_str_list[0] == ('"reason"', '"当前可请求的次数不足"'))
    # """
    # jsonpath取值
    # """
    # ex_json = {'resultcode': '112', 'reason': '当前可请求的次数不足', 'result': None, 'error_code': 10012}
    # a = jsonpath.jsonpath(r_dict, '$.resultcode')
    # print(a)
    # print(f'a: {type(a)}')
    # pytest.assume(a[0] == '112')
    # pprint.pprint(DeepDiff(ex_json, r.json()))
    # pytest.assume(ex_json == r.json())
