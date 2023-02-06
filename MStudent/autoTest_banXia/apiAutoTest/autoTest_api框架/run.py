# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:34
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import sys

import pytest

from MStudent.autoTest_banXia.apiAutoTest.autoTest_api框架.common.file_load import get_yml, write_in_yml

if __name__ == '__main__':
    """
    1、pytest执行后，会自动扫描pytest.ini文件,根据配置的信息执行用例
    2、pytest执行测试用例期间收集结果 pytest test_*.py --alluredir ./reports/shop --clean-alluredir
    3、根据pytest收集的用例结果生成allure报告 allure generate ./reports/shop -o ./reports/html --clean
    4、本地启动服务查看allure报告 allure open -h 127.0.0.1 -p 8883 ./reports/html
    """

    # 获取命令行传递的外部参数
    # 通过终端命令执行 python run.py pro,返回['run.py', 'pro'],即['py文件名', '文件参数']
    args = sys.argv
    print(args)

    # 默认指向 测试环境
    env_file_path = r'/conf/env_test.yml'
    # 传递环境名称 ["test", "pre", "pro"]
    if len(args) > 1:
        env_file_path = get_yml(f'/conf/env_{args[1]}.yml')  # 路径拼接
    # 写入yml文件
    write_in_yml(f'/conf/common.yml', env_file_path["common"])
    write_in_yml(f'/conf/common.yml', env_file_path["http"])
    write_in_yml(f'/conf/db.yml', env_file_path["db"])
    write_in_yml(f'/conf/redis.yml', env_file_path["redis"])

    # pytest.main()  #
    # # 根据执行结果生成allure报告，并输出到./reports/html
    # os.system("allure generate ./reports/shop -o ./reports/html --clean")  # ./ 当前run.py文件所在目录
