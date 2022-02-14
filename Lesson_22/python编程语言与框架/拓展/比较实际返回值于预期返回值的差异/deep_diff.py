# @Author    : House Lee
# -*-coding=utf-8-*-
import pytest
import requests
import pprint
from deepdiff import DeepDiff, grep


class TestDemo(object):
    def setup_class(self):
        self.response = requests.get('http://www.httpbin.org/json').json()

    def test_case_01(self):
        a = {"Object": {
            "code": "0",
            "message": "success"
        },
            "code": "0",
            "message": "success"
        }

        b = {"Object": {
            "code": "0",
            "message": "failure"
        },
            "message": "success",
            "timestamp": "1614301293"
        }

        print("\n\n数据差异为：")
        pprint.pprint(DeepDiff(a, b))

    def test_case_02(self):
        expected_reps = {'slideshow': {'author': 'Yours Truly', 'date': 'date of publication',
                                       'slides': [{'title': 'Wake up to WonderWidgets!', 'type': 'all'}, {
                                           'items': ['Why <em>WonderWidgets</em> are great',
                                                     'Who <em>buys</em> WonderWidgets'], 'title': 'Overview',
                                           'type': 'all'}], 'title': 'Sample Slide Show'}}
        print(f'\n差异为：{DeepDiff(expected_reps, self.response)}\n\n')
        pprint.pprint(DeepDiff(expected_reps, self.response))
        assert self.response == expected_reps
        pytest.assume(self.response == expected_reps)

    def test_case_03(self):
        datas = {"mikezhou": "狂师", "age": 18, "city": "china", "info": {"author": {"tag": "mikezhou"}}}
        reuslt = datas | grep("mike*", use_regexp=True)
        print(f'\n{reuslt}')

