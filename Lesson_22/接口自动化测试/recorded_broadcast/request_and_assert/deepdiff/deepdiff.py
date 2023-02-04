# -*- coding=utf-8 -*-
# @Time    : 2022/07/12 16:02
# @Author  : ╰☆H.俠ゞ
# =============================================================


from deepdiff import DeepDiff
#
# from deepdiff import grep

"""print(dict_a.items)

if DeepDiff(dict_a, dict_b) == {}:
    print("没有差异")
elif DeepDiff(dict_a, dict_b) != {}:
    print("响应错误")


"""
dict_a = {"B": "1"}
dict_b = {"B": "1"}

def test_a():
    print(DeepDiff(dict_a, dict_b))
    assert DeepDiff(dict_a, dict_b) == {}