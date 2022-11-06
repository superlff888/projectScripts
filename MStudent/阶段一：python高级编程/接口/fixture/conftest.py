# -*- coding: utf-8 -*-
"""
author:码同学
date:2022-10-26
desc: 
sample: 
"""
import pytest


def pytest_collection_modifyitems(items):
    """
    该方法解决
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        item._nodeid = item.nodeid.split('::')[0] +'::'+ item.nodeid.split('::')[1].encode("utf-8").decode("unicode_escape")


@pytest.fixture(scope='session', autouse=True)
def realize_session():
    print('session之前')
    yield
    print('session之后')


@pytest.fixture(scope='package', autouse=True)
def realize_package():
    print('package之前')
    yield
    print('package之后')


@pytest.fixture(scope='module', autouse=True)
def realize_module():
    print('module之前')
    yield
    print('module之后')


@pytest.fixture(scope='class', autouse=True)
def realize_class():
    print('class之前')
    yield
    print('class之后')


@pytest.fixture(scope='function', autouse=True)
def realize_function():
    print('function之前')
    yield
    print('function之后')


@pytest.fixture(scope='function', name='aa')
def realize_auto_flase():
    print('autouse=false-function之前')
    yield
    print('autouse=false-function之后')