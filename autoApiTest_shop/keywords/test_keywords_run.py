# !/usr/bin python3                                 
# encoding: utf-8 -*-                            
# @author: 半夏 
# @Time: 2022-11-27 14:38
# @Copyright：北京码同学

# 获取所有测试用例
import pytest

from common.httpClient import RequestsClient
from keywords.keywords_util import get_all_case, get_variables, regx_sub, regx_exec_func

test_data = get_all_case()
print(test_data)

# 如何执行  -- client
client = RequestsClient()
# 获取所有的全局变量
variables = get_variables()


# 参数化
@pytest.mark.parametrize('casename,case_info_list', test_data)
def test_run(casename, case_info_list):
    # case_info_list 是接口流程
    for case_info in case_info_list:
        # 接口地址
        client.url = case_info[0]
        client.url = regx_sub(client.url, variables)
        client.url = regx_exec_func(client.url)

        # 接口方法
        client.method = case_info[1]
        # 接口头信息
        client.headers = case_info[2]
        if client.headers != '':
            client.headers = regx_sub(client.headers, variables)
            client.headers = regx_exec_func(client.headers)
            client.headers = eval(client.headers)

        # 请求参数
        client.api_params = case_info[3]
        if client.api_params != '':
            client.api_params = regx_sub(client.api_params, variables)
            client.api_params = regx_exec_func(client.api_params)
            client.api_params = eval(client.api_params)
            if 'params' in client.api_params:
                client.params = client.api_params['params']

            if 'json' in client.api_params:
                client.json = client.api_params['json']
            if 'data' in client.api_params:
                client.data = client.api_params['data']
            if 'files' in client.api_params:
                client.filesf = client.api_params['files']

        # 发送请求
        resp = client.send()

        # 响应状态码断言
        expect_status = case_info[5]
        assert expect_status == resp.status_code

        # 响应提取  excel读取的数据是字符串  需要转换
        # 响应的数据不是所有的接口都能题 空字符串
        extract_resp = case_info[4]
        if extract_resp != '':

            extract_resp = eval(extract_resp)

            # {"buyerToken":"$.access_token"}
            # 遍历提取字典  注意key保存变量名称 value对应jsonpath表达式
            for key, value in extract_resp.items():
                res = client.extract_json(value)
                variables[key] = res

        # 响应信息断言
        '''[{
            "actual":"$.message",    "expect":"购买数量不能为空"

            }]
        '''
        expect_resp_info = case_info[6]
        if expect_resp_info != '':
            expect_resp_info = eval(expect_resp_info)
            for assert_dict in expect_resp_info:
                expect = assert_dict['expect']
                # 实际结果对应的jsonpath
                json_path = assert_dict['actual']
                # 提取jsonpath 对应的实际值
                actual = client.extract_json(json_path)
                pytest.assume(actual == expect, f'期望结果{expect},实际结果{actual}')
