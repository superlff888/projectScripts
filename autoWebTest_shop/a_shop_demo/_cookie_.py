# -*- coding=utf-8 -*-
# @Time    : 2023/02/19 13:58
# @Author  : ╰☆H.俠ゞ
# =============================================================


from urllib import parse
from selenium import webdriver

driver = webdriver.Chrome()

def url_decode(url_encode):
    return parse.unquote(url_encode)


def add_into_cookie(drivers: webdriver.Chrome(), cookie_dict: dict = None, **kwargs) -> None:
    """
    Usage:
        kwargs = {'k': 'v'}

    """

    print(kwargs)
    cookies_dict = {}
    # {"name": "k", "value": "v"}
    for k in kwargs.keys():
        cookies_dict["name"] = k
        cookies_dict["value"] = kwargs.get(k)
        print(f"cookie_dict: {cookies_dict}")
        drivers.add_cookie(cookies_dict)
    if cookie_dict:
        drivers.add_cookie(cookie_dict)
    driver.refresh()


if __name__ == '__main__':
    add_into_cookie(**{"uid": "123", "access_token": "love8399hvk90wu8h"})
