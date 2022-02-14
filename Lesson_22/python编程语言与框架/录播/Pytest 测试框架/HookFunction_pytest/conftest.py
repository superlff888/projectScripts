# @Time  : 2022/02/11 09:56
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================
from typing import Optional, List

import pytest
import yaml

"""
1、pytest中提供了很多hook接口，具体要在hook函数中实现
2、有部门hook接口会默认实现对应的hook函数，如果我们没有自定义实现hook函数，那就会实现默认hook函数
"""


# pytest_collection收集上来的测试用例实现定制化功能（改写编码，加一些标签……）
def pytest_collection_modifyitems(session: "Session", config: "Config", items: List["Item"]) -> None:
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
    # print(items)
    for item in items:  # 遍历items测试用例列表，name和nodeid是items的属性，即测试用例名字和测试用例的路径
        item.name = item.name.encode('utf-8').decode('unicode-escape')  # encode编码 ； decode 解码（反编码）
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')  # 'unicode-escape' 编码格式支持中文
    items.reverse()  # 调用列表方法，改写用例执行顺序


# 用例执行前
def pytest_runtest_setup(item: "Item") -> None:
    print("hook:setup")


# 用例执行完后
def pytest_runtest_teardown(item: "Item", nextitem: Optional["Item"]) -> None:
    print("hook:teardown")


# 通过pytest_addoption方法来添加命令行参数
def pytest_addoption(parser) -> None:
    """
    Register argparse-style options and ini-style config values,
    called once at the beginning of a test run.

    """
    mygroup = parser.getgroup('hogwarts')  # 所有的option都展示在hogwarts这个group组下

    mygroup.addoption("--env",  # 注册一个命令行（option）选项
                      default='test',  # 命令行参数--env的默认值
                      dest='env',  # 储存的变量，为属性变量，可以使用Option对象访问到这个值，暂时用不到
                      help='set your run env '  # 帮助提示，参数的描述信息
                      )
    mygroup.addoption("--env1",  # 注册一个命令行（option）选项
                      default='dev',  # 命令行参数--env的默认值
                      dest='env',  # 储存的变量，为属性变量，可以使用Option对象访问到这个值，暂时用不到
                      help='set your run env '  # 帮助提示，参数的描述信息
                      )


# 如何针对不同的参数完成不同的逻辑处理
@pytest.fixture(scope='session')  # 通过定义的fixture来获得参数的值
def cmdoption(request):
    result = request.config.getoption("--env")  # 获取我们定义的命令行参数
    return result


# 针对不同的参数值完成不同的逻辑处理
@pytest.fixture(scope='session')
def cmdoption(request):  #
    myenv = request.config.getoption("--env", default='test')  # 利用request获取我们定义的命令行参数,就可以在命令行使用了
    if myenv == 'test':
        datapath = '../datas/test/data.yml'
    if myenv == 'dev':
        datapath = '../datas/dev/data.yml'
    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return myenv, datas


"""
【总结】
1、hook函数名字固定
2、hook函数一般放在项目根目录的conftest.py文件中，hook函数会自动执行
3、执行是有先后顺序的 https://ceshiren.com/t/topic/8807
4、pytest定义了很多hook函数，可以在不同阶段实现不同的功能
"""
