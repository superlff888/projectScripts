# -*- coding=utf-8 -*-
# @Time    : 2022/09/22 14:20
# @Author  : ╰☆H.俠ゞ
# =============================================================
import pytest

from CTTQ.dcsqas.web.Utils.tools import yaml_parse


class Test_yml:

    @pytest.mark.parametrize('obj, value, by_card, timeout, ele, by_text', yaml_parse("./m.yml")["vc"], ids=["test"])
    # @pytest.mark.parametrize('obj, value, by_card, timeout, ele, by_text',
    #                          [[['By.ID', 'u56'], '身份证.png', ['By.ID', 'u58'], 10, ['By.ID', 'u66'], ['By.ID', 'u88']]])
    def test_yml(self, obj, value, by_card, timeout, ele, by_text):
        print(f"{obj}")
        print(f"{value}")
        print(f"{by_card}")
        print(f"{timeout}")
        print(f"{ele}")
        print(f"{by_text}")

    @pytest.mark.parametrize('url,obj', yaml_parse("./m.yml")["login"], ids=["login"])
    def test_login(self, url, obj):
        print(url)
        print(obj)

    @pytest.mark.parametrize('obj, value_title, by_title, by_content, value_content, by_c, timeout, ele, by_text',
                             yaml_parse("./m.yml")["oa"])
    def test_oa(self, obj: tuple, value_title, by_title: tuple, by_content: tuple, value_content, by_c: tuple,
                timeout, ele: tuple, by_text: tuple):
        print(f"{obj}")
        print(f"{value_title}")
        print(f"{by_title}")
        print(f"{by_content}")
        print(f"{value_content}")
        print(f"{by_c}")
        print(f"{timeout}")
        print(f"{ele}")
        print(f"{by_text}")
