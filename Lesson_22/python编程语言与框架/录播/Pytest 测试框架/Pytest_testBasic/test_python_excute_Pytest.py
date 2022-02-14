# @Time  : 2022/01/22 21:36
# @Author    : ╰☆H.俠ゞ
# -*-coding=utf-8-*-
# =============================================================

"""
 【python代码执行pytest】

 - 使用main函数

 - 使用python -m pytest 调用pytest (jenkins持续集成用到)
    相当于执行"pytest"关键字的用例
"""
import pytest


class Test_cases:
    def setup(self):
        print("\nsetup")

    def test_a(self):
        print('\ntest_a')

    @pytest.mark.testB
    def test_b(self):
        print('\ntest_b')

    def teardown(self):
        print('\nteardown')


# print(__name__)

# if __name__ == '__main__':  # 模块入口函数
#     pytest.main()  # 运行当前目录下所有符合条件的用例;相当于 pytest.main(['./']); 注意：to be a list of strings

# if __name__ == '__main__':  # 该模块的入口函数
#     pytest.main(["test_python_excute_Pytest.py::Test_cases", "-vs"])  # 运行模块中的某一条用例

# if __name__ == '__main__':
#     pytest.main(['test_python_excute_Pytest.py::Test_cases::test_a', '-vs'])

# if __name__ == '__main__':
#     pytest.main(['test_python_excute_Pytest.py::Test_cases', '-m', 'testB', '-vs'])
#
# if __name__ == '__main__':
#     print("这是该模块的入口函数")



