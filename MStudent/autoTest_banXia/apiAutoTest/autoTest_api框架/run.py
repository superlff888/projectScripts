# -*- coding=utf-8 -*-
# @Time    : 2023/02/01 10:34
# @Author  : ╰☆H.俠ゞ
# =============================================================
import os
import pytest


if __name__ == '__main__':
    """
    pytest执行测试用例时，会自动扫描pytest.ini文件
    
    allure 报告日志文件格式
    log_format = %(asctime) s [%(filename) s:%(lineno)-4s] [%(levelname) 5s] %(message) s
    log_date_format = %Y-%m-%d %H:%M:%S
    """
    # pytest执行测试用例期间收集结果 pytest test_*.py --alluredir ./reports/shop --clean-alluredir
    pytest.main()
    # 根据执行结果生成allure报告，并输出到./reports/html
    os.system("allure generate ./reports/shop -o ./reports/html --clean")  # ./ 当前run.py文件所在目录