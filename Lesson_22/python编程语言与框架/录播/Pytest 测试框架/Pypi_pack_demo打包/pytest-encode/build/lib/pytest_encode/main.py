# @Time  : 2022/02/12 00:52
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
from typing import List


def pytest_collection_modifyitems(session, config, items) -> None:
    """
    收集上来的测试用例实现改写编码（中文的测试用例名称）；自动添加标签
    :param pytest.Session session: The pytest session object ，即 [pytest] <- 222.ini
    :param _pytest.config.Config config: The pytest config object.
    :param List[pytest.Item] items: List of item objects. 收集的测试用例列表

    print(items)
    （debug）发现需要修改的是：
    name 用例名字
    nodeid  测试用例路径
    """
    print(items)
    for item in items:  # 遍历items测试用例列表，name和nodeid是items的属性，即测试用例名字和测试用例的路径
        item.name = item.name.encode('utf-8').decode('unicode-escape')  # encode编码 ； decode 解码（反编码）
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # 'unicode-escape' 编码格式支持中文
    items.reverse()  # 调用列表方法，改写用例执行顺序