# @Time  : 2021/06/15 13:56
# @Author    : H.侠
# -*-coding=utf-8-*-
# =============================================================


import requests


# base_url = 'http://zwmsqas.cttq.com'

# 新式
from lemonBan.apiTest.lib.logs.loggerMy import MyLogging
from lemonBan.logs.logMutiTest import logger


class HttpRequest(object):
    """
    :类作用： 直接发请求，不记录cookies信息
    :params : 适用于get方法
    :data: 表单形式，一般用于post方法
    :json: json格式，用于post方法
    :url路径拼接 :
        Ⅰ举例 url = urljoin(base_url, '/web/userLoginDetail/login')
        Ⅱ举例 url = os.path.join(base_url, '/web/userLoginDetail/login')
    """
    # url路径拼接
    # url = urljoin(base_url, '/web/userLoginDetail/login')

    def request(self, method, url,
                data=None, params=None, headers=None,
                cookies=None, json=None):
        # 统一将请求方法转化为小写字母
        method = method.lower()
        # 判断请求方法
        if method == 'post':
            # 判断是否为json传参方式
            if json:
                # 打印日志
                logger.info(f'正在发送请求...\n请求方法: {method}, 请求地址: {url}, 请求参数: {json}')
                return requests.post(url, json=json, headers=headers, cookies=cookies)
            else:
                logger.info(f'正在发送请求...\n请求方法: {method}, 请求地址: {url}, 请求参数: {data}')
                return requests.post(url, data=data, headers=headers, cookies=cookies)
        if method == 'get':
            logger.info(f'正在发送请求...\n请求方法: {method}, 请求地址: {url}, 请求参数: {params}')
            return requests.get(url, params=params, headers=headers, cookies=cookies)


class HttpRequestCookies:
    """
    :类作用 :记录cookies信息，提供于下一个请求
    """

    def __init__(self):
        # 创建一个session对象，先用session发起登陆请求 ，然后复用该session

        self.session = requests.sessions.Session()

    def request(self, method, url,
                params=None, data=None, headers=None,
                cookies=None, json=None):
        # 统一将请求方法转化为小写字母
        method = method.lower()
        # 判断请求方法
        if method == 'post':
            # 判断是否为json传参方式
            if json:
                # 打印日志
                logger.info(f'正在发送请求方法{method}, 请求...\n请求方法: {method}, 请求地址: {url},请求参数: {json}')
                return self.session.post(url, json=json, headers=headers, cookies=cookies)
            else:
                logger.info(f'正在发送请求...\n请求方法: {method}, 请求地址: {url},请求参数: {data}')
                return self.session.post(url, data=data, headers=headers, cookies=cookies)
        if method == 'get':
            logger.info(f'正在发送请求...\n请求方法: {method}, 请求地址: {url},请求参数: {params}')
            return self.session.get(url, params=params, headers=headers, cookies=cookies)

    # 用完需要关掉（浏览器/session）
    def close(self):
        self.session.close()


# if __name__ == '__main__':
#     """
#     try异常捕获，前提是要运行目标代码
#     """
#     h = HttpRequest()
#     url = 'http://zwmsqas.cttq.com/web/userLoginDetail/login'
#     data = {"userName": '007', "password": '123456'}
#     response = h.request('post', url=url, data=data)
#     result_json = response.json()
#     result_text = response.text
#     print(f'\njson响应结果为：{result_json}')
#     print(f'\ntext响应结果为：{result_text}')
#     print(f'\njson响应中status为：{result_json["status"]}')
#     print(f'\n响应headers为：{response.headers}')
#     print(f'\n响应headers为：{response.headers["Set-Cookie"]}')
#     print(re.findall('(JSESSIONID=[0-9a-zA-Z]{30,40})', response.headers["Set-Cookie"])[0])
#     print(f'\n响应headers为：{response.cookies}')
#     # assert response.json() == {'status': 0, 'desc': '', 'result': 'wcp/userIndex', 'data': None, 'jsCode': None}
#     pytest.assume(response.json() == {'status': 0, 'desc': '', 'result': 'wcp/userIndex', 'data': None, 'jsCode': None})
#     pytest.assume(result_json["status"] == 0)
