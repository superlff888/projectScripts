# -*- coding=utf-8 -*-
# @Time    : 2022/10/16 14:30
# @Author  : ╰☆H.俠ゞ
# =============================================================


"""实战：测试用例的过滤等操作"""


test = [{'caseName': '测试1', 'order': 2, '开启': '是'}, {'caseName': '测试2',
                                                     'order': 1, '开启': '是'},
        {'caseName': '测试3', 'order': 4, '开启': '否'}, {'caseName': '测试4',
                                                     'order': 3, '开启': '是'}]
# 排除未开启测试用例
new_test = list(filter(lambda elem: elem["开启"] == '是', test))
print(test)
# 排序
test.sort(key=lambda elem: elem['order'])  # 列表的排序方法
print(f"排序后的列表：{test}")


def takeOrder(elem: dict):
    print(elem)
    return elem["order"]


def filterOpen(elem: dict):
    return elem["开启"] == '是'


v1 = takeOrder(test)  # 注意takeOrder()接收的是字典，因为函数返回的是elem["order"]