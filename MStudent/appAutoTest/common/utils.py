# -*- coding=utf-8 -*-
# @Time    : 2023/02/19 15:11
# @Author  : ╰☆H.俠ゞ
# =============================================================
from urllib import parse


def add_into_cookie(driver, cookie_dict: dict = None, **kwargs) -> None:
    """
    注入cookie后，刷新页面

    Usage:
        kwargs = {'k': 'v'}
    """

    cookies_dict = {}
    # {"name": "k", "value": "v"}
    for k in kwargs.keys():
        cookies_dict["name"] = k
        cookies_dict["value"] = kwargs.get(k)
        print(f"cookie_dict: {cookies_dict}")
        driver.add_cookie(cookies_dict)
    if cookie_dict:
        driver.add_cookie(cookie_dict)
    driver.refresh()  # 注入了cookie，所以刷新后，就是登录状态


def url_decode(url_encode):
    """url解码"""
    return parse.unquote(url_encode)