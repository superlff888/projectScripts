# -*- coding=utf-8 -*-
# @Time    : 2022/03/26 16:11
# @Author  : ╰☆H.俠ゞ
# =============================================================
from pprint import pprint

import requests


class TestDmo:

    def test_json(self):
        url = 'https://home.testing-studio.com/categories.json'
        res = requests.get(url=url)
        # pprint(f"\n分类：{res.json()['category_list']['categories'][0]}", indent=2)
        print(f"\n分类：{res.json()['category_list']['categories'][0]}")
        assert res.json()['category_list']['categories'][0]['id'] == 150